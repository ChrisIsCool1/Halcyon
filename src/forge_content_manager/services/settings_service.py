"""Persisted application settings management."""

from __future__ import annotations

import json
from dataclasses import asdict

from forge_content_manager.constants import APPEARANCE_MODES
from forge_content_manager.models import AppSettings, ForgePaths


class SettingsService:
    """Load and save lightweight user settings for the desktop UI."""

    def __init__(self, paths: ForgePaths) -> None:
        """Store the settings file path derived from Forge directories."""
        self._paths = paths

    def load(self) -> AppSettings:
        """Load settings from disk, falling back to defaults when absent or invalid."""
        if not self._paths.settings_file.exists():
            return AppSettings()
        try:
            data = json.loads(self._paths.settings_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return AppSettings()
        appearance_mode = data.get("appearance_mode", "System")
        if appearance_mode not in APPEARANCE_MODES:
            appearance_mode = "System"
        return AppSettings(appearance_mode=appearance_mode)

    def save(self, settings: AppSettings) -> None:
        """Persist application settings to disk."""
        self._paths.settings_file.parent.mkdir(parents=True, exist_ok=True)
        self._paths.settings_file.write_text(json.dumps(asdict(settings), indent=2), encoding="utf-8")
