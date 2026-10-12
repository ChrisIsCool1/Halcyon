"""Image conversion and installation helpers for Forge card art."""

from __future__ import annotations

import logging
from pathlib import Path
from uuid import uuid4

from PIL import Image

from forge_content_manager.models import ForgePaths
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.script_service import make_image_filename, sanitize_display_filename


class ImageService:
    """Install, replace, and locate Forge card images."""

    def __init__(self, paths: ForgePaths, backup_service: BackupService) -> None:
        """Store shared dependencies required for image operations."""
        self._paths = paths
        self._backup_service = backup_service
        self._logger = logging.getLogger(self.__class__.__name__)

    def install_image(self, image_source: Path, set_code: str, card_name: str) -> Path:
        """Convert an input image to Forge's expected JPG naming convention."""
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        base_path = target_dir / make_image_filename(card_name)
        first_variant = target_dir / f"{self._alternate_art_stem(card_name)}1.fullborder.jpg"
        target_path = base_path if base_path.exists() else (first_variant if first_variant.exists() else base_path)
        if target_path.exists():
            self._backup_service.backup_file(target_path)
        with Image.open(image_source) as image:
            converted = image.convert("RGB")
            converted.save(target_path, format="JPEG", quality=95)
        self._logger.info("Installed image %s", target_path)
        return target_path

    def find_image(self, set_code: str, card_name: str) -> Path | None:
        """Locate the expected image path for a given set code and card name."""
        directory = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_path = directory / make_image_filename(card_name)
        if target_path.exists():
            return target_path
        first_variant = directory / f"{self._alternate_art_stem(card_name)}1.fullborder.jpg"
        return first_variant if first_variant.exists() else None

    def install_alternate_art(self, image_source: Path, set_code: str, card_name: str, face_names: list[str] | None = None) -> Path:
        """Install a Forge art variant, numbering the current primary art when needed."""
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        stem = self._alternate_art_stem(card_name)
        base_path = target_dir / make_image_filename(card_name)
        numbered = self._numbered_art_paths(target_dir, card_name)
        legacy = target_dir / f"{stem}.fullborder_alternate.jpg"

        if base_path.exists():
            current_arts = [base_path, *numbered]
            if legacy.exists():
                current_arts.append(legacy)
            self._renumber_art_files(target_dir, stem, current_arts)
            numbered = self._numbered_art_paths(target_dir, card_name)
        elif legacy.exists():
            self._renumber_art_files(target_dir, stem, [*numbered, legacy])
            numbered = self._numbered_art_paths(target_dir, card_name)

        target_index = max((self._art_index(path, stem) or 0 for path in numbered), default=0) + 1
        target_path = target_dir / f"{stem}{target_index}.fullborder.jpg"
        with Image.open(image_source) as image:
            image.convert("RGB").save(target_path, format="JPEG", quality=95)
        for face_name in face_names or []:
            if face_name.casefold() == card_name.casefold():
                continue
            face_stem = self._alternate_art_stem(face_name)
            face_base = target_dir / make_image_filename(face_name)
            source = target_dir / f"{face_stem}1.fullborder.jpg"
            if face_base.exists() and not source.exists():
                self._backup_service.backup_file(face_base)
                face_base.rename(source)
            if source.exists():
                for art_index in range(2, target_index + 1):
                    face_target = target_dir / f"{face_stem}{art_index}.fullborder.jpg"
                    if not face_target.exists():
                        with Image.open(source) as face_image:
                            face_image.convert("RGB").save(face_target, format="JPEG", quality=95)
        return target_path

    def find_alternate_art(self, set_code: str, card_name: str) -> Path | None:
        """Return the first alternate art, retaining the singular compatibility API."""
        arts = self.find_alternate_arts(set_code, card_name)
        return arts[0] if arts else None

    def find_alternate_arts(self, set_code: str, card_name: str) -> list[Path]:
        """Find numbered alternate arts in display order, including legacy art."""
        directory = self._paths.card_images_dir / sanitize_display_filename(set_code)
        stem = self._alternate_art_stem(card_name)
        numbered: list[tuple[int, Path]] = []
        legacy = directory / f"{stem}.fullborder_alternate.jpg"
        for candidate in directory.glob(f"{stem}*.fullborder.jpg"):
            suffix = candidate.name[len(stem):-len(".fullborder.jpg")]
            if suffix.isdigit():
                numbered.append((int(suffix), candidate))
        numbered.sort(key=lambda item: item[0])
        base_path = directory / make_image_filename(card_name)
        if not base_path.exists() and numbered and numbered[0][0] == 1:
            numbered = numbered[1:]
        return [path for _, path in numbered] + ([legacy] if legacy.exists() else [])

    def _numbered_art_paths(self, directory: Path, card_name: str) -> list[Path]:
        """Return all numbered images for a card, including its primary variant."""
        stem = self._alternate_art_stem(card_name)
        numbered = [
            (self._art_index(candidate, stem), candidate)
            for candidate in directory.glob(f"{stem}*.fullborder.jpg")
            if self._art_index(candidate, stem) is not None
        ]
        return [path for _, path in sorted(numbered, key=lambda item: item[0] or 0)]

    def find_numbered_art_paths(self, set_code: str, card_name: str) -> list[Path]:
        """Return every numbered image variant, including the primary art at index 1."""
        directory = self._paths.card_images_dir / sanitize_display_filename(set_code)
        return self._numbered_art_paths(directory, card_name)

    def find_art_variant(self, set_code: str, card_name: str, art_index: int) -> Path | None:
        """Find a one-based card art variant, including a legacy unnumbered primary image."""
        directory = self._paths.card_images_dir / sanitize_display_filename(set_code)
        stem = self._alternate_art_stem(card_name)
        base = directory / make_image_filename(card_name)
        numbered_paths = self._numbered_art_paths(directory, card_name)
        if base.exists() and numbered_paths:
            if art_index == 1:
                return base
            legacy_index = art_index - 1
            if legacy_index <= len(numbered_paths):
                return numbered_paths[legacy_index - 1]
        numbered = directory / f"{stem}{art_index}.fullborder.jpg"
        if numbered.exists():
            return numbered
        if art_index == 1:
            return base if base.exists() else None
        return None

    def replace_art_variant(self, image_source: Path, set_code: str, card_name: str, art_index: int) -> Path:
        """Replace a selected one-based art variant and keep Forge's numbered naming."""
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        stem = self._alternate_art_stem(card_name)
        target_path = target_dir / f"{stem}{art_index}.fullborder.jpg"
        legacy_path = target_dir / make_image_filename(card_name)
        numbered_paths = self._numbered_art_paths(target_dir, card_name)
        if legacy_path.exists() and numbered_paths:
            self._renumber_art_files(target_dir, stem, [legacy_path, *numbered_paths])
        elif legacy_path.exists() and not numbered_paths:
            first_variant = target_dir / f"{stem}1.fullborder.jpg"
            if not first_variant.exists():
                self._backup_service.backup_file(legacy_path)
                legacy_path.rename(first_variant)
        if target_path.exists():
            self._backup_service.backup_file(target_path)
        with Image.open(image_source) as image:
            image.convert("RGB").save(target_path, format="JPEG", quality=95)
        return target_path

    def delete_art_variant(self, set_code: str, card_names: list[str], art_index: int) -> None:
        """Delete a one-based art variant and compact remaining numbered files."""
        directory = self._paths.card_images_dir / sanitize_display_filename(set_code)
        for card_name in dict.fromkeys(card_names):
            stem = self._alternate_art_stem(card_name)
            paths = self._numbered_art_paths(directory, card_name)
            base = directory / make_image_filename(card_name)
            if base.exists() and paths:
                self._renumber_art_files(directory, stem, [base, *paths])
                paths = self._numbered_art_paths(directory, card_name)
            elif base.exists():
                paths = [base]
            if art_index < 1 or art_index > len(paths):
                continue
            removed = paths[art_index - 1]
            if removed.exists():
                self._backup_service.backup_file(removed)
                removed.unlink()
            remaining = paths[:art_index - 1] + paths[art_index:]
            if remaining:
                self._renumber_art_files(directory, stem, remaining)

    @staticmethod
    def _art_index(path: Path, stem: str) -> int | None:
        suffix = path.name[len(stem):-len(".fullborder.jpg")]
        return int(suffix) if suffix.isdigit() else None

    def _renumber_art_files(self, directory: Path, stem: str, paths: list[Path]) -> None:
        """Move existing art files through temporary names to avoid index collisions."""
        temporary_paths: list[tuple[Path, Path]] = []
        for index, source in enumerate(dict.fromkeys(paths), start=1):
            target = directory / f"{stem}{index}.fullborder.jpg"
            if source == target:
                continue
            self._backup_service.backup_file(source)
            temporary = directory / f".{stem}-{uuid4().hex}.tmp"
            source.rename(temporary)
            temporary_paths.append((temporary, target))
        for temporary, target in temporary_paths:
            if target.exists():
                self._backup_service.backup_file(target)
                target.unlink()
            temporary.rename(target)

    def _next_alternate_art_path(self, directory: Path, card_name: str) -> Path:
        stem = self._alternate_art_stem(card_name)
        existing = self.find_alternate_arts(directory.name, card_name)
        used = {int(path.stem[len(stem):]) for path in existing if path.stem[len(stem):].isdigit()}
        index = 1
        while index in used or (directory / f"{stem}{index}.jpg").exists():
            index += 1
        return directory / f"{stem}{index}.fullborder.jpg"

    def rename_alternate_arts(self, set_code: str, old_name: str, new_name: str) -> list[Path]:
        """Rename every numbered alternate art when its card is renamed."""
        renamed: list[Path] = []
        new_stem = self._alternate_art_stem(new_name)
        old_stem = self._alternate_art_stem(old_name)
        for current in self.find_alternate_arts(set_code, old_name):
            self._backup_service.backup_file(current)
            index = self._art_index(current, old_stem)
            suffix = f"{index}" if index is not None else "_alternate"
            target = self._paths.card_images_dir / sanitize_display_filename(set_code) / f"{new_stem}{suffix}.fullborder.jpg"
            if target.exists():
                self._backup_service.backup_file(target)
            current.rename(target)
            renamed.append(target)
        return renamed

    @staticmethod
    def _alternate_art_stem(card_name: str) -> str:
        """Return the card-name portion before Forge's image suffix."""
        filename = make_image_filename(card_name)
        suffix = ".fullborder.jpg"
        return filename[:-len(suffix)] if filename.casefold().endswith(suffix) else Path(filename).stem

    def install_token_image(self, image_source: Path, set_code: str, script_name: str, token_number: int | None) -> Path:
        """Install token art using Forge's numbered token-script filename convention."""
        target_dir = self._paths.token_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        prefix = f"{token_number}_" if token_number is not None else ""
        target_path = target_dir / f"{prefix}{sanitize_display_filename(script_name)}.jpg"
        if target_path.exists():
            self._backup_service.backup_file(target_path)
        with Image.open(image_source) as image:
            image.convert("RGB").save(target_path, format="JPEG", quality=95)
        return target_path

    def find_token_image(self, set_code: str, script_name: str, token_number: int | None) -> Path | None:
        target_dir = self._paths.token_images_dir / sanitize_display_filename(set_code)
        names = ([f"{token_number}_{sanitize_display_filename(script_name)}.jpg"] if token_number is not None else []) + [f"{sanitize_display_filename(script_name)}.jpg"]
        return next((target_dir / name for name in names if (target_dir / name).exists()), None)

    def rename_image(self, current_path: Path, set_code: str, card_name: str, previous_card_name: str | None = None) -> Path | None:
        """Rename an existing image when a card name changes."""
        if not current_path.exists():
            return None
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        current_stem = self._alternate_art_stem(previous_card_name) if previous_card_name else ""
        current_index = self._art_index(current_path, current_stem) if current_stem else None
        target_stem = self._alternate_art_stem(card_name)
        target_path = target_dir / (f"{target_stem}{current_index}.fullborder.jpg" if current_index is not None else make_image_filename(card_name))
        if current_path == target_path:
            return current_path
        sibling_variants = self._numbered_art_paths(target_dir, previous_card_name) if previous_card_name else []
        if target_path.exists():
            self._backup_service.backup_file(target_path)
            target_path.unlink()
        self._backup_service.backup_file(current_path)
        current_path.rename(target_path)
        for variant in sibling_variants:
            if variant == current_path:
                continue
            index = self._art_index(variant, current_stem)
            if index is None:
                continue
            sibling_target = target_dir / f"{target_stem}{index}.fullborder.jpg"
            if sibling_target.exists():
                self._backup_service.backup_file(sibling_target)
                sibling_target.unlink()
            self._backup_service.backup_file(variant)
            variant.rename(sibling_target)
        return target_path
