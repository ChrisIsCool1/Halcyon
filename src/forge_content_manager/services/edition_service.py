"""Edition file parsing and writing helpers for Forge custom sets."""

from __future__ import annotations

import logging
from pathlib import Path

from forge_content_manager.constants import SET_TYPE_CUSTOM
from forge_content_manager.models import EditionCardEntry, EditionDocument, ForgePaths, ForgeSetRecord
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.script_service import make_set_filename


class EditionService:
    """Manage Forge edition metadata files stored under the custom editions folder."""

    def __init__(self, paths: ForgePaths, backup_service: BackupService) -> None:
        """Store path dependencies and logging facilities."""
        self._paths = paths
        self._backup_service = backup_service
        self._logger = logging.getLogger(self.__class__.__name__)

    def list_sets(self) -> list[ForgeSetRecord]:
        """Load all custom sets from the Forge editions directory."""
        results: list[ForgeSetRecord] = []
        for file_path in sorted(self._paths.custom_editions_dir.glob("*.txt")):
            document = self.parse_edition_file(file_path)
            results.append(
                ForgeSetRecord(
                    name=document.metadata.get("Name", file_path.stem),
                    code=document.metadata.get("Code", ""),
                    date=document.metadata.get("Date", ""),
                    set_type=document.metadata.get("Type", SET_TYPE_CUSTOM),
                    card_count=len(document.cards),
                    file_path=file_path,
                )
            )
        return results

    def create_set(self, name: str, code: str, date_value: str, set_type: str = SET_TYPE_CUSTOM) -> ForgeSetRecord:
        """Create a new custom set edition file."""
        file_path = self._paths.custom_editions_dir / make_set_filename(name)
        if file_path.exists():
            raise FileExistsError(f"A set named '{name}' already exists.")
        document = EditionDocument(
            metadata={"Code": code, "Name": name, "Date": date_value, "Type": set_type or SET_TYPE_CUSTOM},
            cards=[],
            file_path=file_path,
        )
        self.write_document(document, backup_existing=False)
        return ForgeSetRecord(name=name, code=code, date=date_value, set_type=set_type, card_count=0, file_path=file_path)

    def parse_edition_file(self, file_path: Path) -> EditionDocument:
        """Parse an edition file from disk into structured metadata and card entries."""
        return self.parse_edition_text(file_path.read_text(encoding="utf-8"), file_path)

    def parse_edition_text(self, content: str, file_path: Path | None = None) -> EditionDocument:
        """Parse edition content from raw text."""
        metadata: dict[str, str] = {}
        cards: list[EditionCardEntry] = []
        section = ""
        for raw_line in content.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith("[") and line.endswith("]"):
                section = line.casefold()
                continue
            if section == "[metadata]" and "=" in line:
                key, value = line.split("=", 1)
                metadata[key.strip()] = value.strip()
                continue
            if section == "[cards]":
                parts = line.split(maxsplit=2)
                if len(parts) == 3 and parts[0].isdigit():
                    cards.append(
                        EditionCardEntry(
                            collector_number=int(parts[0]),
                            rarity_code=parts[1],
                            card_name=parts[2],
                        )
                    )
        return EditionDocument(metadata=metadata, cards=cards, file_path=file_path)

    def serialize_document(self, document: EditionDocument) -> str:
        """Serialize an edition document back into Forge's text format."""
        metadata_lines = [
            f"Code={document.metadata.get('Code', '')}",
            f"Name={document.metadata.get('Name', '')}",
            f"Date={document.metadata.get('Date', '')}",
            f"Type={document.metadata.get('Type', SET_TYPE_CUSTOM)}",
        ]
        card_lines = [
            f"{entry.collector_number} {entry.rarity_code} {entry.card_name}"
            for entry in sorted(document.cards, key=lambda item: item.collector_number)
        ]
        return "\n".join(["[metadata]", *metadata_lines, "", "[cards]", *card_lines, ""])

    def write_document(self, document: EditionDocument, backup_existing: bool = True) -> None:
        """Write a parsed edition document to disk, backing up prior content when requested."""
        if document.file_path is None:
            raise ValueError("Edition document has no file path.")
        document.file_path.parent.mkdir(parents=True, exist_ok=True)
        if backup_existing and document.file_path.exists():
            self._backup_service.backup_file(document.file_path)
        document.file_path.write_text(self.serialize_document(document), encoding="utf-8")
        self._logger.info("Wrote edition file %s", document.file_path)

    def update_set_metadata(
        self,
        file_path: Path,
        name: str,
        code: str,
        date_value: str,
        set_type: str,
    ) -> ForgeSetRecord:
        """Update metadata for an existing custom set, renaming the edition file if necessary."""
        document = self.parse_edition_file(file_path)
        document.metadata.update({"Name": name, "Code": code, "Date": date_value, "Type": set_type or SET_TYPE_CUSTOM})
        new_file_path = file_path.parent / make_set_filename(name)
        if new_file_path != file_path and new_file_path.exists():
            raise FileExistsError(f"A set named '{name}' already exists.")
        if new_file_path != file_path:
            self._backup_service.backup_file(file_path)
            file_path.rename(new_file_path)
            document.file_path = new_file_path
        self.write_document(document)
        return ForgeSetRecord(name=name, code=code, date=date_value, set_type=set_type, card_count=len(document.cards), file_path=new_file_path)

    def add_or_update_card(self, file_path: Path, card_name: str, rarity_code: str) -> EditionCardEntry:
        """Add a new card to a set or update the existing rarity if it is already present."""
        document = self.parse_edition_file(file_path)
        existing = next((card for card in document.cards if card.card_name.casefold() == card_name.casefold()), None)
        if existing is not None:
            existing.rarity_code = rarity_code
            self.write_document(document)
            return existing
        collector_number = max((card.collector_number for card in document.cards), default=0) + 1
        new_entry = EditionCardEntry(collector_number=collector_number, rarity_code=rarity_code, card_name=card_name)
        document.cards.append(new_entry)
        self.write_document(document)
        return new_entry

    def remove_card(self, file_path: Path, card_name: str) -> bool:
        """Remove a card entry from the provided edition file."""
        document = self.parse_edition_file(file_path)
        remaining_cards = [card for card in document.cards if card.card_name.casefold() != card_name.casefold()]
        if len(remaining_cards) == len(document.cards):
            return False
        for index, card in enumerate(remaining_cards, start=1):
            card.collector_number = index
        document.cards = remaining_cards
        self.write_document(document)
        return True

    def rename_card_references(self, old_name: str, new_name: str) -> int:
        """Rename card references across all custom set edition files."""
        updated_files = 0
        for set_record in self.list_sets():
            document = self.parse_edition_file(set_record.file_path)
            changed = False
            for entry in document.cards:
                if entry.card_name.casefold() == old_name.casefold():
                    entry.card_name = new_name
                    changed = True
            if changed:
                self.write_document(document)
                updated_files += 1
        return updated_files

    def find_sets_for_card(self, card_name: str) -> list[ForgeSetRecord]:
        """Return all custom sets that reference the specified card name."""
        matches: list[ForgeSetRecord] = []
        for set_record in self.list_sets():
            document = self.parse_edition_file(set_record.file_path)
            if any(entry.card_name.casefold() == card_name.casefold() for entry in document.cards):
                matches.append(set_record)
        return matches
