"""Constants used throughout Halcyon."""

from __future__ import annotations

from typing import Final

APP_NAME: Final[str] = "Halcyon"
APP_VERSION: Final[str] = "0.1.0"
SET_TYPE_CUSTOM: Final[str] = "Custom"
PACKAGE_EXTENSION: Final[str] = ".forgepkg.zip"
SETTINGS_FILENAME: Final[str] = "forge_content_manager_settings.json"
LOG_FILENAME: Final[str] = "forge_content_manager.log"
RARITY_LABELS: Final[tuple[str, ...]] = (
    "Common",
    "Uncommon",
    "Rare",
    "Mythic",
    "Special",
)
RARITY_CODES: Final[dict[str, str]] = {
    "Common": "C",
    "Uncommon": "U",
    "Rare": "R",
    "Mythic": "M",
    "Special": "S",
}
RARITY_CODES_REVERSED: Final[dict[str, str]] = {value: key for key, value in RARITY_CODES.items()}
APPEARANCE_MODES: Final[tuple[str, ...]] = ("System", "Light", "Dark")
