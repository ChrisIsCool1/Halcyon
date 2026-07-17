"""High-level application workflows used by the customtkinter UI."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable

from forge_content_manager.constants import RARITY_CODES
from forge_content_manager.models import (
    BatchImportSummary,
    CardImportInput,
    CardRecord,
    CollisionStrategy,
    ForgePaths,
    ForgeSetRecord,
    ImportCardResult,
    PackageImportSummary,
)
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.image_service import ImageService
from forge_content_manager.services.package_service import PackageService
from forge_content_manager.services.script_service import (
    extract_card_name,
    make_script_filename,
    normalize_card_name,
    resolve_script_path,
    validate_script,
)

ProgressCallback = Callable[[int, int, str], None]


class ForgeContentService:
    """Facade that coordinates the application's core Forge content workflows."""

    def __init__(
        self,
        paths: ForgePaths,
        backup_service: BackupService,
        edition_service: EditionService,
        image_service: ImageService,
        package_service: PackageService,
    ) -> None:
        """Store all service dependencies needed by the UI layer."""
        self.paths = paths
        self.backup_service = backup_service
        self.edition_service = edition_service
        self.image_service = image_service
        self.package_service = package_service
        self._logger = logging.getLogger(self.__class__.__name__)

    def list_sets(self) -> list[ForgeSetRecord]:
        """Return all custom sets currently installed in Forge."""
        return self.edition_service.list_sets()

    def create_set(self, name: str, code: str, date_value: str, set_type: str) -> ForgeSetRecord:
        """Create a new custom set."""
        return self.edition_service.create_set(name=name, code=code, date_value=date_value, set_type=set_type)

    def update_set(self, file_path: Path, name: str, code: str, date_value: str, set_type: str) -> ForgeSetRecord:
        """Update metadata for an existing custom set."""
        return self.edition_service.update_set_metadata(file_path, name=name, code=code, date_value=date_value, set_type=set_type)

    def import_cards(
        self,
        destination_set: ForgeSetRecord,
        cards: list[CardImportInput],
        progress_callback: ProgressCallback | None = None,
    ) -> BatchImportSummary:
        """Import a batch of custom cards into the selected Forge set."""
        results: list[ImportCardResult] = []
        imported_count = 0
        failed_count = 0
        total = len(cards)
        for index, card in enumerate(cards, start=1):
            card_name = extract_card_name(card.script_text) or f"Card {index}"
            if progress_callback is not None:
                progress_callback(index - 1, total, f"Importing {card_name}")
            messages = validate_script(card.script_text, destination_set.name, card.image_source)
            errors = [message.message for message in messages if message.level == "error"]
            warnings = [message.message for message in messages if message.level == "warning"]
            if errors:
                results.append(ImportCardResult(card_name=card_name, success=False, warnings=warnings, error="; ".join(errors)))
                failed_count += 1
                continue
            script_path = resolve_script_path(self.paths.custom_cards_dir, card_name)
            script_path.parent.mkdir(parents=True, exist_ok=True)
            if script_path.exists():
                self.backup_service.backup_file(script_path)
            script_path.write_text(card.script_text, encoding="utf-8")
            if card.image_source is not None:
                self.image_service.install_image(card.image_source, destination_set.code, card_name)
            self.edition_service.add_or_update_card(destination_set.file_path, card_name, RARITY_CODES[card.rarity])
            results.append(ImportCardResult(card_name=card_name, success=True, warnings=warnings))
            imported_count += 1
            self._logger.info("Imported custom card %s into set %s", card_name, destination_set.name)
        if progress_callback is not None:
            progress_callback(total, total, "Import complete")
        return BatchImportSummary(
            destination_set=destination_set.name,
            imported_count=imported_count,
            failed_count=failed_count,
            results=results,
        )

    def scan_cards(self) -> list[CardRecord]:
        """Scan installed custom card scripts and map them to known sets and images."""
        set_lookup: dict[str, list[ForgeSetRecord]] = {}
        for set_record in self.list_sets():
            document = self.edition_service.parse_edition_file(set_record.file_path)
            for card in document.cards:
                key = normalize_card_name(card.card_name)
                set_lookup.setdefault(key, []).append(set_record)
        records: list[CardRecord] = []
        for script_path in sorted(self.paths.custom_cards_dir.rglob("*.txt")):
            script_text = script_path.read_text(encoding="utf-8")
            card_name = extract_card_name(script_text) or script_path.stem
            normalized_name = normalize_card_name(card_name)
            matching_sets = set_lookup.get(normalized_name, [])
            primary_set = matching_sets[0] if matching_sets else None
            set_name = ", ".join({record.name for record in matching_sets}) if matching_sets else "Unassigned"
            set_code = primary_set.code if primary_set is not None else ""
            image_path = self.image_service.find_image(set_code, card_name) if set_code else None
            records.append(
                CardRecord(
                    name=card_name,
                    normalized_name=normalized_name,
                    script_path=script_path,
                    image_path=image_path,
                    image_present=image_path is not None,
                    set_name=set_name,
                    set_code=set_code,
                )
            )
        return records

    def get_card_rarity(self, set_file_path: Path, card_name: str) -> str:
        """Return the display rarity for a card in a set."""
        from forge_content_manager.constants import RARITY_CODES_REVERSED

        document = self.edition_service.parse_edition_file(set_file_path)
        entry = next((card for card in document.cards if card.card_name.casefold() == card_name.casefold()), None)
        if entry is None:
            raise ValueError(f"Card '{card_name}' is not in the selected set.")
        return RARITY_CODES_REVERSED.get(entry.rarity_code.upper(), entry.rarity_code)

    def update_card_rarity(self, set_file_path: Path, card_name: str, rarity: str) -> None:
        """Update a card's rarity in one set."""
        if rarity not in RARITY_CODES:
            raise ValueError(f"Unknown rarity: {rarity}")
        self.edition_service.add_or_update_card(set_file_path, card_name, RARITY_CODES[rarity])

    def load_script(self, script_path: Path) -> str:
        """Load a custom card script from disk."""
        return script_path.read_text(encoding="utf-8")

    def save_script(self, card: CardRecord, new_text: str) -> CardRecord:
        """Save an edited card script, renaming related files if the card name changes."""
        new_name = extract_card_name(new_text)
        if not new_name:
            raise ValueError("Edited script is missing a Name field.")
        old_name = card.name
        validation_messages = validate_script(new_text, card.set_name if card.set_name != "Unassigned" else "Edited Card", None)
        errors = [message.message for message in validation_messages if message.level == "error"]
        if errors:
            raise ValueError("; ".join(errors))
        new_script_path = resolve_script_path(self.paths.custom_cards_dir, new_name)
        if new_script_path != card.script_path and new_script_path.exists():
            self.backup_service.backup_file(new_script_path)
        self.backup_service.backup_file(card.script_path)
        new_script_path.parent.mkdir(parents=True, exist_ok=True)
        new_script_path.write_text(new_text, encoding="utf-8")
        if new_script_path != card.script_path and card.script_path.exists():
            card.script_path.unlink()
        if old_name.casefold() != new_name.casefold():
            self.edition_service.rename_card_references(old_name, new_name)
            if card.image_path is not None and card.set_code:
                card.image_path = self.image_service.rename_image(card.image_path, card.set_code, new_name)
        return CardRecord(
            name=new_name,
            normalized_name=normalize_card_name(new_name),
            script_path=new_script_path,
            image_path=card.image_path,
            image_present=card.image_path is not None and card.image_path.exists(),
            set_name=card.set_name,
            set_code=card.set_code,
        )

    def replace_image(self, card: CardRecord, image_source: Path) -> CardRecord:
        """Replace or install the image associated with a card."""
        if not card.set_code:
            raise ValueError("Card is not associated with a set, so its image target cannot be resolved.")
        image_path = self.image_service.install_image(image_source, card.set_code, card.name)
        return CardRecord(
            name=card.name,
            normalized_name=card.normalized_name,
            script_path=card.script_path,
            image_path=image_path,
            image_present=True,
            set_name=card.set_name,
            set_code=card.set_code,
        )

    def delete_card(self, card: CardRecord) -> None:
        """Delete a card script and its associated image, while updating edition files."""
        self.backup_service.backup_file(card.script_path)
        if card.script_path.exists():
            card.script_path.unlink()
        if card.image_path is not None and card.image_path.exists():
            self.backup_service.backup_file(card.image_path)
            card.image_path.unlink()
        for set_record in self.edition_service.find_sets_for_card(card.name):
            self.edition_service.remove_card(set_record.file_path, card.name)

    def delete_set(self, set_record: ForgeSetRecord) -> None:
        """Delete a custom set and remove uniquely-owned assets referenced by it."""
        document = self.edition_service.parse_edition_file(set_record.file_path)
        for card_entry in document.cards:
            other_sets = [record for record in self.edition_service.find_sets_for_card(card_entry.card_name) if record.file_path != set_record.file_path]
            script_path = resolve_script_path(self.paths.custom_cards_dir, card_entry.card_name)
            if not other_sets and script_path.exists():
                self.backup_service.backup_file(script_path)
                script_path.unlink()
            image_path = self.image_service.find_image(set_record.code, card_entry.card_name)
            if image_path is not None and image_path.exists():
                self.backup_service.backup_file(image_path)
                image_path.unlink()
        self.backup_service.backup_file(set_record.file_path)
        set_record.file_path.unlink(missing_ok=True)

    def export_set_package(self, set_record: ForgeSetRecord, output_path: Path) -> Path:
        """Export a custom set to a distributable Forge package."""
        return self.package_service.export_set_package(set_record.file_path, output_path)

    def import_set_package(self, package_file: Path, strategy: CollisionStrategy) -> PackageImportSummary:
        """Import a Forge package archive into the local custom content directories."""
        return self.package_service.import_set_package(package_file, strategy)
