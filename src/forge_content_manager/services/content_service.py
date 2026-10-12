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
    ValidationMessage,
)
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.image_service import ImageService
from forge_content_manager.services.package_service import PackageService
from forge_content_manager.services.forge_paths import ensure_directories
from forge_content_manager.services.script_service import (
    extract_card_name,
    extract_card_face_names,
    make_script_filename,
    normalize_card_name,
    normalize_edition_card_name,
    resolve_script_path,
    resolve_token_script_path,
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

    def reconfigure(self, paths: ForgePaths) -> None:
        """Switch all content workflows to a newly selected set of folders."""
        ensure_directories(paths)
        backup_service = BackupService(paths)
        edition_service = EditionService(paths, backup_service)
        image_service = ImageService(paths, backup_service)
        package_service = PackageService(paths, backup_service, edition_service)
        self.paths = paths
        self.backup_service = backup_service
        self.edition_service = edition_service
        self.image_service = image_service
        self.package_service = package_service

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
            alternate_art_sources = [*card.alternate_art_sources, *([card.alternate_art_source] if card.alternate_art_source else [])]
            if progress_callback is not None:
                progress_callback(index - 1, total, f"Importing {card_name}")
            messages = validate_script(card.script_text, destination_set.name, card.image_source, card.alternate_image_source)
            for alternate_source in alternate_art_sources:
                if not alternate_source.exists():
                    messages.append(ValidationMessage(level="error", message=f"Alternate art image does not exist: {alternate_source}"))
            errors = [message.message for message in messages if message.level == "error"]
            warnings = [message.message for message in messages if message.level == "warning"]
            if errors:
                results.append(ImportCardResult(card_name=card_name, success=False, warnings=warnings, error="; ".join(errors)))
                failed_count += 1
                continue
            is_token = card.content_type == "token"
            token_script_name = (card.token_script_name or "").strip()
            if is_token and card.alternate_image_source is not None:
                results.append(ImportCardResult(card_name=card_name, success=False, warnings=warnings, error="Tokens cannot have an alternate card image."))
                failed_count += 1
                continue
            if is_token and alternate_art_sources:
                results.append(ImportCardResult(card_name=card_name, success=False, warnings=warnings, error="Tokens cannot have alternate card art."))
                failed_count += 1
                continue
            if is_token and not token_script_name:
                results.append(ImportCardResult(card_name=card_name, success=False, warnings=warnings, error="Token script name is required."))
                failed_count += 1
                continue
            script_path = (
                resolve_token_script_path(self.paths.custom_tokens_dir, token_script_name)
                if is_token else resolve_script_path(self.paths.custom_cards_dir, card_name)
            )
            script_path.parent.mkdir(parents=True, exist_ok=True)
            if script_path.exists():
                self.backup_service.backup_file(script_path)
            script_path.write_text(card.script_text, encoding="utf-8")
            if is_token:
                token_entry = self.edition_service.add_or_update_token(destination_set.file_path, token_script_name)
                if card.image_source is not None:
                    self.image_service.install_token_image(card.image_source, destination_set.code, token_script_name, token_entry.collector_number)
            else:
                if card.image_source is not None:
                    self.image_service.install_image(card.image_source, destination_set.code, card_name)
                face_names = extract_card_face_names(card.script_text)
                if card.alternate_image_source is not None:
                    self.image_service.install_image(card.alternate_image_source, destination_set.code, face_names[1])
                for alternate_source in alternate_art_sources:
                    self.image_service.install_alternate_art(alternate_source, destination_set.code, card_name, face_names)
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
                key = normalize_edition_card_name(card.card_name)
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
            face_names = extract_card_face_names(script_text) or [card_name]
            image_paths = [self.image_service.find_image(set_code, face_name) if set_code else None for face_name in face_names]
            records.append(
                CardRecord(
                    name=card_name,
                    normalized_name=normalized_name,
                    script_path=script_path,
                    image_path=image_path,
                    image_present=bool(image_paths) and all(path is not None for path in image_paths),
                    set_name=set_name,
                    set_code=set_code,
                    face_names=face_names,
                    image_paths=image_paths,
                    alternate_art_paths=self.image_service.find_alternate_arts(set_code, card_name) if set_code else [],
                )
            )
        token_records_by_path: dict[Path, CardRecord] = {}
        for set_record in self.list_sets():
            document = self.edition_service.parse_edition_file(set_record.file_path)
            for token in document.tokens:
                script_path = next(
                    (path for path in self.paths.custom_tokens_dir.rglob("*.txt") if path.stem.casefold() == token.script_name.casefold()),
                    resolve_token_script_path(self.paths.custom_tokens_dir, token.script_name),
                )
                if not script_path.exists():
                    continue
                existing_record = token_records_by_path.get(script_path)
                if existing_record is not None:
                    set_names = existing_record.set_name.split(", ")
                    if set_record.name not in set_names:
                        existing_record.set_name = f"{existing_record.set_name}, {set_record.name}"
                    continue
                script_text = script_path.read_text(encoding="utf-8")
                name = extract_card_name(script_text) or token.script_name
                image_path = self.image_service.find_token_image(set_record.code, token.script_name, token.collector_number)
                record = CardRecord(
                    name=name, normalized_name=normalize_card_name(token.script_name), script_path=script_path,
                    image_path=image_path, image_present=image_path is not None, set_name=set_record.name,
                    set_code=set_record.code, content_type="token", token_script_name=token.script_name,
                )
                token_records_by_path[script_path] = record
                records.append(record)
        return records

    def get_card_rarity(self, set_file_path: Path, card_name: str) -> str:
        """Return the display rarity for a card in a set."""
        from forge_content_manager.constants import RARITY_CODES_REVERSED

        document = self.edition_service.parse_edition_file(set_file_path)
        normalized_name = normalize_card_name(card_name)
        entry = next((card for card in document.cards if normalize_edition_card_name(card.card_name) == normalized_name), None)
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
        old_face_names = card.face_names or extract_card_face_names(self.load_script(card.script_path)) or [old_name]
        new_face_names = extract_card_face_names(new_text) or [new_name]
        validation_messages = validate_script(new_text, card.set_name if card.set_name != "Unassigned" else "Edited Card", None)
        errors = [message.message for message in validation_messages if message.level == "error"]
        if errors:
            raise ValueError("; ".join(errors))
        new_script_path = (
            resolve_token_script_path(self.paths.custom_tokens_dir, card.token_script_name or card.script_path.stem)
            if card.content_type == "token" else resolve_script_path(self.paths.custom_cards_dir, new_name)
        )
        if new_script_path != card.script_path and new_script_path.exists():
            self.backup_service.backup_file(new_script_path)
        self.backup_service.backup_file(card.script_path)
        new_script_path.parent.mkdir(parents=True, exist_ok=True)
        new_script_path.write_text(new_text, encoding="utf-8")
        if new_script_path != card.script_path and card.script_path.exists():
            card.script_path.unlink()
        if card.content_type == "card":
            if old_name.casefold() != new_name.casefold():
                self.edition_service.rename_card_references(old_name, new_name)
            if card.set_code:
                for old_face_name, new_face_name in zip(old_face_names, new_face_names):
                    existing_image = self.image_service.find_image(card.set_code, old_face_name)
                    if existing_image is not None:
                        self.image_service.rename_image(existing_image, card.set_code, new_face_name, old_face_name)
                self.image_service.rename_alternate_arts(card.set_code, old_name, new_name)
        return CardRecord(
            name=new_name,
            normalized_name=normalize_card_name(new_name),
            script_path=new_script_path,
            image_path=self.image_service.find_image(card.set_code, new_name) if card.set_code else None,
            image_present=bool(new_face_names) and all(self.image_service.find_image(card.set_code, face_name) is not None for face_name in new_face_names) if card.set_code else False,
            set_name=card.set_name,
            set_code=card.set_code,
            content_type=card.content_type,
            token_script_name=card.token_script_name,
            face_names=new_face_names,
            image_paths=[self.image_service.find_image(card.set_code, face_name) if card.set_code else None for face_name in new_face_names],
            alternate_art_paths=self.image_service.find_alternate_arts(card.set_code, new_name) if card.set_code else [],
        )

    def get_card_art_labels(self, card: CardRecord) -> list[str]:
        """Return the edition caption for each art entry associated with a card."""
        if card.content_type != "card" or not card.set_code:
            return [card.name]
        set_record = next((item for item in self.list_sets() if item.code == card.set_code), None)
        return self.edition_service.get_card_art_labels(set_record.file_path, card.name) if set_record else [card.name]

    def get_card_art_entry_paths(self, card: CardRecord, face_index: int = 0) -> list[Path | None]:
        """Return the selected face image path matching each edition art row."""
        labels = self.get_card_art_labels(card)
        if not card.set_code:
            return [card.image_path]
        face_names = card.face_names or [card.name]
        if face_index < 0 or face_index >= len(face_names):
            raise ValueError("Selected card face does not exist.")
        face_name = face_names[face_index]
        return [
            self.image_service.find_art_variant(card.set_code, face_name, index)
            for index in range(1, len(labels) + 1)
        ]

    def replace_card_art_entry(self, card: CardRecord, image_source: Path, art_index: int, face_index: int = 0) -> None:
        """Replace one face image for a selected edition art entry."""
        if card.content_type != "card" or not card.set_code:
            raise ValueError("Card art cannot be resolved for the selected entry.")
        face_names = card.face_names or [card.name]
        if face_index < 0 or face_index >= len(face_names):
            raise ValueError("Selected card face does not exist.")
        self.image_service.replace_art_variant(image_source, card.set_code, face_names[face_index], art_index)

    def delete_card_art_entry(self, card: CardRecord, set_file_path: Path, art_index: int) -> None:
        """Delete a selected edition art row and its corresponding image variants."""
        if card.content_type != "card" or not card.set_code:
            raise ValueError("Only card art entries can be deleted.")
        self.edition_service.remove_card_art_entry(set_file_path, card.name, art_index)
        self.image_service.delete_art_variant(card.set_code, card.face_names or [card.name], art_index)

    def replace_image(self, card: CardRecord, image_source: Path, face_index: int = 0) -> CardRecord:
        """Replace or install the image associated with a card."""
        if not card.set_code:
            raise ValueError("Card is not associated with a set, so its image target cannot be resolved.")
        if card.content_type == "token":
            document = next((self.edition_service.parse_edition_file(item.file_path) for item in self.list_sets() if item.code == card.set_code), None)
            token = next((item for item in document.tokens if item.script_name == card.token_script_name), None) if document else None
            image_path = self.image_service.install_token_image(image_source, card.set_code, card.token_script_name or card.script_path.stem, token.collector_number if token else None)
        else:
            face_names = card.face_names or [card.name]
            if face_index < 0 or face_index >= len(face_names):
                raise ValueError("Selected card face does not exist.")
            image_path = self.image_service.install_image(image_source, card.set_code, face_names[face_index])
        image_paths = list(card.image_paths) or [card.image_path]
        while len(image_paths) <= face_index:
            image_paths.append(None)
        image_paths[face_index] = image_path
        return CardRecord(
            name=card.name,
            normalized_name=card.normalized_name,
            script_path=card.script_path,
            image_path=image_path,
            image_present=all(path is not None and path.exists() for path in image_paths),
            set_name=card.set_name,
            set_code=card.set_code,
            content_type=card.content_type,
            token_script_name=card.token_script_name,
            face_names=card.face_names,
            image_paths=image_paths,
        )

    def replace_alternate_art(self, card: CardRecord, image_source: Path, set_file_path: Path, rarity_code: str) -> CardRecord:
        """Install alternate art for a card independently of its faces."""
        if card.content_type != "card":
            raise ValueError("Tokens cannot have alternate card art.")
        if not card.set_code:
            raise ValueError("Card is not associated with a set, so its image target cannot be resolved.")
        self.image_service.install_alternate_art(image_source, card.set_code, card.name, card.face_names)
        alternate_art_paths = self.image_service.find_alternate_arts(card.set_code, card.name)
        self.edition_service.add_alternate_art_entries(
            set_file_path,
            card.name,
            rarity_code,
            [path.name.removesuffix(".fullborder.jpg") for path in alternate_art_paths],
        )
        return CardRecord(
            name=card.name, normalized_name=card.normalized_name, script_path=card.script_path,
            image_path=card.image_path, image_present=card.image_present, set_name=card.set_name,
            set_code=card.set_code, face_names=card.face_names, image_paths=card.image_paths,
            alternate_art_paths=alternate_art_paths, content_type=card.content_type,
        )

    def delete_card(self, card: CardRecord) -> None:
        """Delete a card script and its associated image, while updating edition files."""
        self.backup_service.backup_file(card.script_path)
        if card.script_path.exists():
            card.script_path.unlink()
        image_paths = {path for path in card.image_paths if path is not None}
        if card.image_path is not None:
            image_paths.add(card.image_path)
        if card.content_type == "card" and card.set_code:
            for face_name in card.face_names or [card.name]:
                image_paths.update(self.image_service.find_numbered_art_paths(card.set_code, face_name))
        for image_path in image_paths:
            if image_path.exists():
                self.backup_service.backup_file(image_path)
                image_path.unlink()
        alternate_arts = card.alternate_art_paths or (self.image_service.find_alternate_arts(card.set_code, card.name) if card.set_code else [])
        for alternate_art in alternate_arts:
            if alternate_art.exists():
                self.backup_service.backup_file(alternate_art)
                alternate_art.unlink()
        if card.content_type == "token":
            for set_record in self.edition_service.find_sets_for_token(card.token_script_name or card.script_path.stem):
                self.edition_service.remove_token(set_record.file_path, card.token_script_name or card.script_path.stem)
        else:
            for set_record in self.edition_service.find_sets_for_card(card.name):
                self.edition_service.remove_card(set_record.file_path, card.name)

    def delete_set(self, set_record: ForgeSetRecord) -> None:
        """Delete a custom set and remove uniquely-owned assets referenced by it."""
        document = self.edition_service.parse_edition_file(set_record.file_path)
        seen_cards: set[str] = set()
        for card_entry in document.cards:
            card_name = card_entry.card_name.partition("@")[0].rstrip()
            normalized_name = normalize_edition_card_name(card_name)
            if normalized_name in seen_cards:
                continue
            seen_cards.add(normalized_name)
            other_sets = [record for record in self.edition_service.find_sets_for_card(card_name) if record.file_path != set_record.file_path]
            script_path = resolve_script_path(self.paths.custom_cards_dir, card_name)
            script_text = script_path.read_text(encoding="utf-8") if script_path.exists() else ""
            if not other_sets and script_path.exists():
                self.backup_service.backup_file(script_path)
                script_path.unlink()
            face_names = extract_card_face_names(script_text) or [card_name]
            for face_name in face_names:
                image_path = self.image_service.find_image(set_record.code, face_name)
                if image_path is not None and image_path.exists():
                    self.backup_service.backup_file(image_path)
                    image_path.unlink()
                for image_path in self.image_service.find_numbered_art_paths(set_record.code, face_name):
                    if image_path.exists():
                        self.backup_service.backup_file(image_path)
                        image_path.unlink()
            for alternate_art in self.image_service.find_alternate_arts(set_record.code, card_name):
                self.backup_service.backup_file(alternate_art)
                alternate_art.unlink()
        for token_entry in document.tokens:
            other_sets = [record for record in self.edition_service.find_sets_for_token(token_entry.script_name) if record.file_path != set_record.file_path]
            script_path = resolve_token_script_path(self.paths.custom_tokens_dir, token_entry.script_name)
            if not other_sets and script_path.exists():
                self.backup_service.backup_file(script_path)
                script_path.unlink()
            image_path = self.image_service.find_token_image(set_record.code, token_entry.script_name, token_entry.collector_number)
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

    def export_set_pack(self, set_records: list[ForgeSetRecord], output_path: Path) -> Path:
        """Export multiple selected sets in Forge's custom/pics folder layout."""
        return self.package_service.export_set_pack([record.file_path for record in set_records], output_path)

    def import_set_pack(self, source: Path, strategy: CollisionStrategy) -> PackageImportSummary:
        """Import a Forge-style custom/pics set pack."""
        return self.package_service.import_set_pack(source, strategy)
