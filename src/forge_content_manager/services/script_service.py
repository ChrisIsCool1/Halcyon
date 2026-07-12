"""Script parsing and validation helpers that preserve Forge logic text."""

from __future__ import annotations

import re
from pathlib import Path

from forge_content_manager.models import ValidationMessage

INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*]')
NON_ALNUM = re.compile(r"[^a-z0-9]+")
MULTI_UNDERSCORE = re.compile(r"_+")


def extract_metadata_fields(script_text: str) -> dict[str, str]:
    """Extract only selected metadata fields from a Forge script without parsing gameplay logic."""
    fields: dict[str, str] = {}
    for line in script_text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key in {"Name", "Types", "Oracle", "ManaCost"} and key not in fields:
            fields[key] = value.strip()
    return fields


def extract_card_name(script_text: str) -> str | None:
    """Extract the card name from the first Name field in a Forge script."""
    return extract_metadata_fields(script_text).get("Name")


def validate_script(
    script_text: str,
    destination_set: str | None,
    image_source: Path | None,
) -> list[ValidationMessage]:
    """Perform basic structural validation for a Forge script import."""
    fields = extract_metadata_fields(script_text)
    messages: list[ValidationMessage] = []
    card_name = fields.get("Name")
    if not fields.get("Name"):
        messages.append(ValidationMessage(level="error", message="Missing required Name field."))
    if not fields.get("Types"):
        messages.append(
            ValidationMessage(level="error", message="Missing required Types field.", card_name=card_name)
        )
    if not destination_set:
        messages.append(
            ValidationMessage(level="error", message="No destination set selected.", card_name=card_name)
        )
    if image_source is not None and not image_source.exists():
        messages.append(
            ValidationMessage(level="error", message="Selected image file does not exist.", card_name=card_name)
        )
    if not fields.get("Oracle"):
        messages.append(
            ValidationMessage(level="warning", message="Missing Oracle field.", card_name=card_name)
        )
    if not fields.get("ManaCost"):
        messages.append(
            ValidationMessage(level="warning", message="Missing ManaCost field.", card_name=card_name)
        )
    return messages


def normalize_card_name(card_name: str) -> str:
    """Convert a card name into the standard Forge custom script filename stem."""
    stem = NON_ALNUM.sub("_", card_name.casefold()).strip("_")
    normalized = MULTI_UNDERSCORE.sub("_", stem)
    return normalized or "card"


def make_script_filename(card_name: str) -> str:
    """Build the on-disk filename for a custom Forge script."""
    return f"{normalize_card_name(card_name)}.txt"


def resolve_script_path(cards_dir: Path, card_name: str) -> Path:
    """Resolve the canonical Forge path for a custom card script."""
    filename = make_script_filename(card_name)
    folder_name = filename[0] if filename and filename[0].isalnum() else "_"
    return cards_dir / folder_name / filename


def sanitize_display_filename(value: str) -> str:
    """Remove Windows-invalid filename characters while keeping readable names."""
    sanitized = INVALID_FILENAME_CHARS.sub("", value).strip().rstrip(".")
    return sanitized or "Unnamed"


def make_image_filename(card_name: str) -> str:
    """Build the Forge fullborder image filename for a card."""
    return f"{sanitize_display_filename(card_name)}.fullborder.jpg"


def make_set_filename(set_name: str) -> str:
    """Build a safe edition filename for the provided set name."""
    return f"{sanitize_display_filename(set_name)}.txt"
