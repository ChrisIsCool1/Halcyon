"""Script parsing and validation helpers that preserve Forge logic text."""

from __future__ import annotations

import re
from pathlib import Path

from forge_content_manager.models import ValidationMessage

INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*]')
NON_ALNUM = re.compile(r"[^a-z0-9]+")
MULTI_UNDERSCORE = re.compile(r"_+")


def extract_metadata_fields(script_text: str) -> dict[str, str]:
    """Extract selected metadata without interpreting gameplay logic.

    Args:
        script_text: Complete Forge script text.

    Returns:
        The first value found for each supported metadata field.
    """
    fields: dict[str, str] = {}
    for line in script_text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key in {"Name", "Types", "Oracle", "ManaCost"} and key not in fields:
            fields[key] = value.strip()
    return fields


def extract_card_name(script_text: str) -> str | None:
    """Extract the first ``Name`` field from a Forge script.

    Args:
        script_text: Complete Forge script text.

    Returns:
        The card name, or ``None`` when the field is absent.
    """
    return extract_metadata_fields(script_text).get("Name")


def validate_script(
    script_text: str,
    destination_set: str | None,
    image_source: Path | None,
) -> list[ValidationMessage]:
    """Perform metadata and file checks before importing a card.

    Args:
        script_text: Complete Forge script text to inspect.
        destination_set: Selected set name, or ``None`` when no set is selected.
        image_source: Optional source image that will be installed.

    Returns:
        Errors and warnings suitable for display in the import workflow.
    """
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
    """Convert a display name to Forge's canonical filename stem.

    Args:
        card_name: Display name from the script's ``Name`` field.

    Returns:
        A lowercase, underscore-separated stem; ``"card"`` for an empty result.
    """
    stem = NON_ALNUM.sub("_", card_name.casefold()).strip("_")
    normalized = MULTI_UNDERSCORE.sub("_", stem)
    return normalized or "card"


def make_script_filename(card_name: str) -> str:
    """Build the canonical ``.txt`` filename for a custom card script.

    Args:
        card_name: Display name of the card.

    Returns:
        A normalized filename ending in ``.txt``.
    """
    return f"{normalize_card_name(card_name)}.txt"


def resolve_script_path(cards_dir: Path, card_name: str) -> Path:
    """Resolve the canonical nested path for a custom card script.

    Args:
        cards_dir: Root of Forge's custom cards directory.
        card_name: Display name of the card.

    Returns:
        The path under the filename's first-character folder.
    """
    filename = make_script_filename(card_name)
    # Forge groups scripts by the first filename character rather than a flat directory.
    folder_name = filename[0] if filename and filename[0].isalnum() else "_"
    return cards_dir / folder_name / filename


def resolve_token_script_path(tokens_dir: Path, script_name: str) -> Path:
    """Resolve a token script path, retaining Forge's token script identifier."""
    stem = sanitize_display_filename(Path(script_name).stem)
    return tokens_dir / f"{stem}.txt"


def sanitize_display_filename(value: str) -> str:
    """Remove Windows-invalid characters while retaining a readable name.

    Args:
        value: Name to use in a Windows filename.

    Returns:
        A safe non-empty filename component.
    """
    sanitized = INVALID_FILENAME_CHARS.sub("", value).strip().rstrip(".")
    return sanitized or "Unnamed"


def make_image_filename(card_name: str) -> str:
    """Build Forge's ``.fullborder.jpg`` filename for a card.

    Args:
        card_name: Display name of the card.

    Returns:
        A sanitized image filename.
    """
    return f"{sanitize_display_filename(card_name)}.fullborder.jpg"


def make_set_filename(set_name: str) -> str:
    """Build a safe ``.txt`` edition filename.

    Args:
        set_name: Display name of the set.

    Returns:
        A sanitized edition filename.
    """
    return f"{sanitize_display_filename(set_name)}.txt"
