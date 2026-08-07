"""Persisted application settings management."""

from __future__ import annotations

import json
from dataclasses import asdict, fields
from pathlib import Path

from forge_content_manager.constants import APPEARANCE_MODES
from forge_content_manager.models import AppSettings, ForgePaths

_FORGE_PATH_FIELDS = (
    "custom_cards_dir",
    "custom_tokens_dir",
    "custom_editions_dir",
    "custom_starter_decks_dir",
    "card_images_dir",
    "token_images_dir",
    "backups_dir",
    "logs_dir",
)


class SettingsService:
    """Load and save lightweight user settings for the desktop UI."""

    def __init__(self, paths: ForgePaths, settings_file: Path | None = None) -> None:
        """Store the settings file path derived from Forge directories."""
        self._paths = paths
        self._settings_file = settings_file or paths.settings_file

    @property
    def paths(self) -> ForgePaths:
        """Return the currently active Forge paths."""
        return self._paths

    def set_paths(self, paths: ForgePaths) -> None:
        """Update the active Forge paths without moving the settings file."""
        self._paths = paths

    def resolve_paths(self, settings: AppSettings | None = None) -> ForgePaths:
        """Apply persisted folder choices to the supplied or loaded defaults."""
        settings = settings or self.load()
        overrides = {
            field_name: getattr(settings, field_name)
            for field_name in _FORGE_PATH_FIELDS
            if getattr(settings, field_name) is not None
        }
        return ForgePaths(
            **{
                field_name: overrides.get(field_name, getattr(self._paths, field_name))
                for field_name in (field.name for field in fields(ForgePaths))
            }
        )

    def load(self) -> AppSettings:
        """Load settings from disk, falling back to defaults when absent or invalid."""
        if not self._settings_file.exists():
            return AppSettings()
        try:
            data = json.loads(self._settings_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return AppSettings()
        if not isinstance(data, dict):
            return AppSettings()
        appearance_mode = data.get("appearance_mode", "System")
        if appearance_mode not in APPEARANCE_MODES:
            appearance_mode = "System"
        path_values = {
            field_name: self._path_setting(data.get(field_name))
            for field_name in ("reference_cards_dir", "documentation_pack_source", *_FORGE_PATH_FIELDS)
        }
        return AppSettings(appearance_mode=appearance_mode, **path_values)

    def save(self, settings: AppSettings) -> None:
        """Persist application settings to disk."""
        self._settings_file.parent.mkdir(parents=True, exist_ok=True)
        data = asdict(settings)
        for field_name in ("reference_cards_dir", "documentation_pack_source", *_FORGE_PATH_FIELDS):
            value = getattr(settings, field_name)
            if value is not None:
                data[field_name] = str(value)
        self._settings_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @staticmethod
    def _path_setting(value: object) -> Path | None:
        return Path(value) if isinstance(value, str) and value else None
