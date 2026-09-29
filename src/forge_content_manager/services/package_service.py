"""Import and export of Forge custom content packages."""

from __future__ import annotations

import json
import logging
import shutil
import tempfile
from dataclasses import asdict
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from forge_content_manager.constants import PACKAGE_EXTENSION
from forge_content_manager.models import CollisionStrategy, ForgePaths, PackageImportSummary, PackageManifest
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.script_service import (
    extract_card_name,
    extract_card_face_names,
    make_image_filename,
    make_script_filename,
    make_set_filename,
    normalize_card_name,
    resolve_script_path,
    sanitize_display_filename,
)


class PackageService:
    """Handle .forgepkg.zip export and import operations."""

    def __init__(
        self,
        paths: ForgePaths,
        backup_service: BackupService,
        edition_service: EditionService,
    ) -> None:
        """Store shared service dependencies for package workflows."""
        self._paths = paths
        self._backup_service = backup_service
        self._edition_service = edition_service
        self._logger = logging.getLogger(self.__class__.__name__)

    def export_set_package(self, set_file: Path, output_path: Path) -> Path:
        """Create a Forge package archive for a single custom set."""
        document = self._edition_service.parse_edition_file(set_file)
        output_file = output_path
        if output_file.suffix != ".zip" or not output_file.name.endswith(PACKAGE_EXTENSION):
            output_file = output_file.with_name(f"{output_file.stem}{PACKAGE_EXTENSION}")
        manifest = PackageManifest(
            name=document.metadata.get("Name", set_file.stem),
            code=document.metadata.get("Code", ""),
            version=1,
            card_count=len(document.cards),
        )
        with ZipFile(output_file, "w", compression=ZIP_DEFLATED) as archive:
            archive.writestr("manifest.json", json.dumps(asdict(manifest), indent=2))
            archive.writestr("edition.txt", set_file.read_text(encoding="utf-8"))
            for card in document.cards:
                script_path = resolve_script_path(self._paths.custom_cards_dir, card.card_name)
                if script_path.exists():
                    archive.write(script_path, f"cards/{script_path.relative_to(self._paths.custom_cards_dir).as_posix()}")
                script_text = script_path.read_text(encoding="utf-8") if script_path.exists() else ""
                for face_name in extract_card_face_names(script_text) or [card.card_name]:
                    image_path = self._paths.card_images_dir / sanitize_display_filename(manifest.code) / make_image_filename(face_name)
                    if image_path.exists():
                        archive.write(image_path, f"images/{image_path.name}")
        self._logger.info("Exported set package %s", output_file)
        return output_file

    def export_set_pack(self, set_files: list[Path], output_path: Path) -> Path:
        """Export selected sets in the folder layout used by Forge GitHub packs."""
        output_file = output_path if output_path.suffix.casefold() == ".zip" else output_path.with_suffix(".zip")
        written: set[str] = set()
        scripts_by_name: dict[str, list[Path]] = {}
        for script in self._paths.custom_cards_dir.rglob("*.txt"):
            name = extract_card_name(script.read_text(encoding="utf-8"))
            if name:
                scripts_by_name.setdefault(name.casefold(), []).append(script)
        with ZipFile(output_file, "w", compression=ZIP_DEFLATED) as archive:
            for set_file in set_files:
                document = self._edition_service.parse_edition_file(set_file)
                archive.write(set_file, f"custom/editions/{set_file.name}")
                code = sanitize_display_filename(document.metadata.get("Code", ""))
                for image in (self._paths.card_images_dir / code).glob("*"):
                    archive_name = f"pics/cards/{code}/{image.name}"
                    if image.is_file() and archive_name not in written:
                        archive.write(image, archive_name)
                        written.add(archive_name)
                token_image_dir = self._paths.token_images_dir / code
                if token_image_dir.is_dir():
                    for image in token_image_dir.glob("*"):
                        archive_name = f"pics/tokens/{code}/{image.name}"
                        if image.is_file() and archive_name not in written:
                            archive.write(image, archive_name)
                            written.add(archive_name)
                for card in document.cards:
                    scripts = scripts_by_name.get(card.card_name.casefold(), [])
                    for script in scripts:
                        archive_name = f"custom/cards/{script.relative_to(self._paths.custom_cards_dir).as_posix()}"
                        if archive_name not in written:
                            archive.write(script, archive_name)
                            written.add(archive_name)
                        text = script.read_text(encoding="utf-8")
                for token in document.tokens:
                    for script in self._paths.custom_tokens_dir.rglob("*.txt"):
                        if script.stem.casefold() == token.script_name.casefold():
                            archive_name = f"custom/tokens/{script.relative_to(self._paths.custom_tokens_dir).as_posix()}"
                            if archive_name not in written:
                                archive.write(script, archive_name)
                                written.add(archive_name)
        return output_file

    def import_set_pack(self, source: Path, strategy: CollisionStrategy) -> PackageImportSummary:
        """Import a folder or ZIP containing Forge-style custom/ and pics/ trees."""
        with tempfile.TemporaryDirectory(prefix="halcyon-set-pack-") as temp_name:
            root = Path(temp_name)
            if source.is_dir():
                pack_root = source
            else:
                with ZipFile(source) as archive:
                    for member in archive.infolist():
                        parts = Path(member.filename.replace("\\", "/")).parts
                        if ".." in parts or Path(member.filename).is_absolute():
                            raise ValueError("Pack contains an unsafe path.")
                    archive.extractall(root)
                pack_root = root
            custom_dir, pics_dir = self._find_pack_folders(pack_root)
            if custom_dir is None and pics_dir is None:
                raise ValueError("Pack must contain a custom folder, a pics folder, or both.")
            installed_cards = installed_images = 0
            skipped: list[str] = []
            warnings: list[str] = []
            for source_dir, target_dir, category in (
                (custom_dir, self._paths.custom_root_dir or self._paths.custom_cards_dir.parent, "custom"),
                (pics_dir, self._paths.pics_dir or self._paths.card_images_dir.parent, "pics"),
            ):
                if source_dir is None:
                    continue
                for file in source_dir.rglob("*"):
                    if not file.is_file():
                        continue
                    relative = file.relative_to(source_dir)
                    target = target_dir / relative
                    if target.exists() and strategy == "skip":
                        skipped.append(f"Skipped existing {category}/{relative.as_posix()}")
                        continue
                    if target.exists() and strategy == "replace":
                        self._backup_service.backup_file(target)
                    if target.exists() and strategy == "rename":
                        target = self._unique_named_path(target)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file, target)
                    if category == "custom" and "cards" in relative.parts and file.suffix.casefold() == ".txt":
                        installed_cards += 1
                    elif category == "pics":
                        installed_images += 1
            return PackageImportSummary(
                imported_set_name=f"Set pack ({installed_cards} card scripts)", imported_set_code="",
                installed_cards=installed_cards, installed_images=installed_images,
                skipped_items=skipped, warnings=warnings,
            )

    @staticmethod
    def _find_pack_folders(root: Path) -> tuple[Path | None, Path | None]:
        """Find the custom and pics directories, allowing a GitHub ZIP wrapper folder."""
        if root.name.casefold() in {"custom", "pics"}:
            sibling = root.parent / ("pics" if root.name.casefold() == "custom" else "custom")
            return (root if root.name.casefold() == "custom" else sibling if sibling.is_dir() else None,
                    root if root.name.casefold() == "pics" else sibling if sibling.is_dir() else None)
        candidates = [root, *[item for item in root.iterdir() if item.is_dir()]]
        custom = next((item / "custom" for item in candidates if (item / "custom").is_dir()), None)
        pics = next((item / "pics" for item in candidates if (item / "pics").is_dir()), None)
        return custom, pics

    def import_set_package(self, package_file: Path, strategy: CollisionStrategy) -> PackageImportSummary:
        """Install a Forge package archive using the chosen collision strategy."""
        with ZipFile(package_file, "r") as archive:
            names = set(archive.namelist())
            if "manifest.json" not in names or "edition.txt" not in names:
                raise ValueError("Package must contain manifest.json and edition.txt.")
            manifest_data = json.loads(archive.read("manifest.json").decode("utf-8"))
            edition_text = archive.read("edition.txt").decode("utf-8")
            document = self._edition_service.parse_edition_text(edition_text)
            set_name = document.metadata.get("Name") or manifest_data.get("name", "Imported Set")
            set_code = document.metadata.get("Code") or manifest_data.get("code", "CUSTOM")
            target_file = self._paths.custom_editions_dir / make_set_filename(set_name)

            if strategy == "skip" and target_file.exists():
                return PackageImportSummary(
                    imported_set_name=set_name,
                    imported_set_code=set_code,
                    installed_cards=0,
                    installed_images=0,
                    skipped_items=[f"Skipped package because set '{set_name}' already exists."],
                )

            if strategy == "rename" and target_file.exists():
                set_name = self._unique_set_name(set_name)
                set_code = self._unique_set_code(set_code)
                document.metadata["Name"] = set_name
                document.metadata["Code"] = set_code
                target_file = self._paths.custom_editions_dir / make_set_filename(set_name)

            if strategy == "replace" and target_file.exists():
                self._backup_service.backup_file(target_file)

            installed_cards = 0
            installed_images = 0
            skipped_items: list[str] = []
            warnings: list[str] = []

            for item_name in sorted(name for name in names if name.startswith("cards/") and name.endswith(".txt")):
                script_text = archive.read(item_name).decode("utf-8")
                card_name = extract_card_name(script_text)
                if not card_name:
                    warnings.append(f"Skipped package script without Name field: {item_name}")
                    continue
                target_script = resolve_script_path(self._paths.custom_cards_dir, card_name)
                if strategy == "rename" and target_script.exists():
                    target_script = self._unique_script_path(target_script)
                elif strategy == "skip" and target_script.exists():
                    skipped_items.append(f"Skipped card script for {card_name}")
                    continue
                elif strategy == "replace" and target_script.exists():
                    self._backup_service.backup_file(target_script)
                target_script.parent.mkdir(parents=True, exist_ok=True)
                target_script.write_text(script_text, encoding="utf-8")
                installed_cards += 1

            image_target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
            image_target_dir.mkdir(parents=True, exist_ok=True)
            for item_name in sorted(name for name in names if name.startswith("images/")):
                target_image = image_target_dir / Path(item_name).name
                if strategy == "rename" and target_image.exists():
                    target_image = self._unique_named_path(target_image)
                elif strategy == "skip" and target_image.exists():
                    skipped_items.append(f"Skipped image {target_image.name}")
                    continue
                elif strategy == "replace" and target_image.exists():
                    self._backup_service.backup_file(target_image)
                target_image.write_bytes(archive.read(item_name))
                installed_images += 1

            document.file_path = target_file
            target_file.write_text(self._edition_service.serialize_document(document), encoding="utf-8")
            self._logger.info("Imported set package %s into %s", package_file, target_file)
            return PackageImportSummary(
                imported_set_name=set_name,
                imported_set_code=set_code,
                installed_cards=installed_cards,
                installed_images=installed_images,
                skipped_items=skipped_items,
                warnings=warnings,
            )

    def _unique_set_name(self, base_name: str) -> str:
        """Generate a unique set name for a renamed package import."""
        counter = 2
        candidate = f"{base_name} Imported"
        while (self._paths.custom_editions_dir / make_set_filename(candidate)).exists():
            candidate = f"{base_name} Imported {counter}"
            counter += 1
        return candidate

    def _unique_set_code(self, base_code: str) -> str:
        """Generate a unique set code for a renamed package import."""
        existing_codes = {set_record.code.casefold() for set_record in self._edition_service.list_sets()}
        candidate = f"{base_code}_2"
        counter = 3
        while candidate.casefold() in existing_codes:
            candidate = f"{base_code}_{counter}"
            counter += 1
        return candidate

    def _unique_script_path(self, path: Path) -> Path:
        """Generate a non-conflicting script path when importing with rename semantics."""
        return self._unique_named_path(path)

    def _unique_named_path(self, path: Path) -> Path:
        """Generate a unique sibling path by appending a numeric suffix."""
        counter = 2
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        while candidate.exists():
            counter += 1
            candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        return candidate
