"""Dataclasses used by the Forge content management workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

AppearanceMode = Literal["System", "Light", "Dark"]
CollisionStrategy = Literal["skip", "replace", "rename"]
MessageLevel = Literal["error", "warning", "info"]


@dataclass(slots=True)
class ForgePaths:
    """Filesystem locations used by Forge custom content and the manager app."""

    custom_cards_dir: Path
    custom_editions_dir: Path
    custom_starter_decks_dir: Path
    card_images_dir: Path
    backups_dir: Path
    logs_dir: Path
    settings_file: Path


@dataclass(slots=True)
class EditionCardEntry:
    """A single card entry inside a Forge edition file."""

    collector_number: int
    rarity_code: str
    card_name: str


@dataclass(slots=True)
class EditionDocument:
    """Parsed contents of a Forge edition file."""

    metadata: dict[str, str]
    cards: list[EditionCardEntry]
    file_path: Path | None = None


@dataclass(slots=True)
class ForgeSetRecord:
    """User-facing summary for a Forge custom set."""

    name: str
    code: str
    date: str
    set_type: str
    card_count: int
    file_path: Path


@dataclass(slots=True)
class CardRecord:
    """Discovered custom card information for the browser tab."""

    name: str
    normalized_name: str
    script_path: Path
    image_path: Path | None
    image_present: bool
    set_name: str
    set_code: str


@dataclass(slots=True)
class CardImportInput:
    """User-supplied input for importing a single custom card."""

    script_text: str
    image_source: Path | None
    rarity: str


@dataclass(slots=True)
class ValidationMessage:
    """Validation feedback produced while handling card scripts."""

    level: MessageLevel
    message: str
    card_name: str | None = None


@dataclass(slots=True)
class ImportCardResult:
    """Outcome of importing one card script."""

    card_name: str
    success: bool
    warnings: list[str] = field(default_factory=list)
    error: str | None = None


@dataclass(slots=True)
class BatchImportSummary:
    """Aggregate results from a batch card import operation."""

    destination_set: str
    imported_count: int
    failed_count: int
    results: list[ImportCardResult] = field(default_factory=list)


@dataclass(slots=True)
class PackageManifest:
    """Serializable metadata for an exported Forge package."""

    name: str
    code: str
    version: int
    card_count: int


@dataclass(slots=True)
class PackageImportSummary:
    """Outcome details for a package import operation."""

    imported_set_name: str
    imported_set_code: str
    installed_cards: int
    installed_images: int
    skipped_items: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class AppSettings:
    """Persisted UI settings for the desktop application."""

    appearance_mode: AppearanceMode = "System"
