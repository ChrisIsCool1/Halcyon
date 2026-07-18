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
