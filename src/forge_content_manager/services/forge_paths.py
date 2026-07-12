"""Helpers for resolving and creating Forge-specific filesystem paths."""

from __future__ import annotations

import os
from pathlib import Path

from forge_content_manager.constants import LOG_FILENAME, SETTINGS_FILENAME
from forge_content_manager.models import ForgePaths


def get_forge_paths() -> ForgePaths:
    """Resolve the Forge custom content directories from the Windows environment."""
    appdata = Path(os.environ.get("APPDATA", Path.home()))
    localappdata = Path(os.environ.get("LOCALAPPDATA", Path.home()))
    forge_custom_root = appdata / "Forge" / "custom"
    logs_dir = forge_custom_root / "logs"
    paths = ForgePaths(
        custom_cards_dir=forge_custom_root / "cards",
        custom_editions_dir=forge_custom_root / "editions",
        custom_starter_decks_dir=forge_custom_root / "starterdecks",
        card_images_dir=localappdata / "Forge" / "Cache" / "pics" / "cards",
        backups_dir=forge_custom_root / "backups",
        logs_dir=logs_dir,
        settings_file=forge_custom_root / SETTINGS_FILENAME,
    )
    ensure_directories(paths)
    return paths


def ensure_directories(paths: ForgePaths) -> None:
    """Create any required Forge directories that do not already exist."""
    for directory in (
        paths.custom_cards_dir,
        paths.custom_editions_dir,
        paths.custom_starter_decks_dir,
        paths.card_images_dir,
        paths.backups_dir,
        paths.logs_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    (paths.logs_dir / LOG_FILENAME).touch(exist_ok=True)
