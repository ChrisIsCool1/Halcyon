"""Image conversion and installation helpers for Forge card art."""

from __future__ import annotations

import logging
from pathlib import Path

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
        target_path = target_dir / make_image_filename(card_name)
        if target_path.exists():
            self._backup_service.backup_file(target_path)
        with Image.open(image_source) as image:
            converted = image.convert("RGB")
            converted.save(target_path, format="JPEG", quality=95)
        self._logger.info("Installed image %s", target_path)
        return target_path

    def find_image(self, set_code: str, card_name: str) -> Path | None:
        """Locate the expected image path for a given set code and card name."""
        target_path = self._paths.card_images_dir / sanitize_display_filename(set_code) / make_image_filename(card_name)
        return target_path if target_path.exists() else None

    def install_alternate_art(self, image_source: Path, set_code: str, card_name: str) -> Path:
        """Append a numbered alternate art image beside the card's primary art."""
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = self._next_alternate_art_path(target_dir, card_name)
        with Image.open(image_source) as image:
            image.convert("RGB").save(target_path, format="JPEG", quality=95)
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
        return [path for _, path in numbered] + ([legacy] if legacy.exists() else [])

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
        for index, current in enumerate(self.find_alternate_arts(set_code, old_name), start=1):
            self._backup_service.backup_file(current)
            target = self._paths.card_images_dir / sanitize_display_filename(set_code) / f"{new_stem}{index}.fullborder.jpg"
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

    def rename_image(self, current_path: Path, set_code: str, card_name: str) -> Path | None:
        """Rename an existing image when a card name changes."""
        if not current_path.exists():
            return None
        target_dir = self._paths.card_images_dir / sanitize_display_filename(set_code)
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / make_image_filename(card_name)
        if current_path == target_path:
            return current_path
        if target_path.exists():
            self._backup_service.backup_file(target_path)
        self._backup_service.backup_file(current_path)
        current_path.rename(target_path)
        return target_path
