"""Build, validate, and read compact script-editor documentation packs."""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path


PACK_FORMAT = "forge-script-documentation"
PACK_VERSION = "2"


@dataclass(frozen=True, slots=True)
class DocumentationRecord:
    """One searchable documentation entry stored in a pack."""

    name: str
    category: str
    description: str
    parameters: tuple[str, ...] = ()
    optional_parameters: tuple[str, ...] = ()
    example: str | None = None
    scope: str = "*"


def validate_pack(path: Path) -> str:
    """Return a pack's display version or raise ValueError when it is invalid."""
    try:
        connection = sqlite3.connect(f"file:{path.resolve().as_posix()}?mode=ro", uri=True)
        try:
            metadata = dict(connection.execute("SELECT key, value FROM metadata"))
            columns = {row[1] for row in connection.execute("PRAGMA table_info(documentation)")}
        finally:
            connection.close()
    except (OSError, sqlite3.Error) as exc:
        raise ValueError(f"Not a readable documentation pack: {exc}") from exc
    if metadata.get("format") != PACK_FORMAT or metadata.get("format_version") != PACK_VERSION:
        raise ValueError("This file is not a compatible Forge script documentation pack.")
    required = {"name", "category", "description", "scope", "parameters", "optional_parameters", "example"}
    if not required.issubset(columns):
        raise ValueError("This documentation pack is missing required records.")
    return metadata.get("content_version", "unversioned")


def load_pack(path: Path) -> list[DocumentationRecord]:
    """Load all records from a validated pack."""
    validate_pack(path)
    connection = sqlite3.connect(path)
    try:
        rows = connection.execute(
            "SELECT name, category, description, scope, parameters, optional_parameters, example FROM documentation"
        ).fetchall()
    finally:
        connection.close()
    return [
        DocumentationRecord(row[0], row[1], row[2], tuple(filter(None, row[4].split("\x1f"))),
                            tuple(filter(None, row[5].split("\x1f"))), row[6] or None, row[3])
        for row in rows
    ]


def parse_markdown_catalog(root: Path) -> list[DocumentationRecord]:
    """Read authored category Markdown files using compact heading-based entries."""
    records: list[DocumentationRecord] = []
    if not root.is_dir():
        return records
    for path in sorted(root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        scope_match = re.search(r"(?mi)^<!--\s*forge-doc-scope:\s*([A-Za-z]+):?\s*-->\s*$", text)
        scope = scope_match.group(1) if scope_match else "*"
        sections = re.split(r"(?m)^##\s+`?(.+?)`?\s*$", text)
        for index in range(1, len(sections), 2):
            name, body = sections[index].strip(), sections[index + 1].strip()
            lines = [line.strip() for line in body.splitlines()]
            description = next((line for line in lines if line and not line.startswith(("**Signature:**", "**Example:**", "<!--"))), "")
            signature = next((line.removeprefix("**Signature:**").strip().strip("`") for line in lines if line.startswith("**Signature:**")), "")
            example = next((line.removeprefix("**Example:**").strip().strip("`") for line in lines if line.startswith("**Example:**")), None)
            category = path.stem.replace("-", " ").title()
            records.append(DocumentationRecord(name, category, description, tuple(filter(None, signature.split(" | "))), (), example, scope))
    return records


def parse_legacy_guides(root: Path) -> list[DocumentationRecord]:
    """Preserve the existing bundled guide headings in compiled packs."""
    guide_names = ("Card-scripting-API.md", "AbilityFactory.md", "Triggers.md", "Targeting.md", "Statics.md", "Replacements.md", "Costs.md")
    records: list[DocumentationRecord] = [
        DocumentationRecord(name, "Card property", description)
        for name, description in {
            "Name": "Card display name.", "ManaCost": "Mana cost shown in mana shards.",
            "Types": "Space-separated card types and subtypes.", "PT": "Power and toughness.",
            "Oracle": "Oracle text displayed by Forge.", "Colors": "Color indicator for cards without a mana cost.",
            "K": "Keyword ability; use one K: line per keyword.", "A": "Spell or activated ability.",
            "T": "Triggered ability.", "S": "Static ability.", "R": "Replacement effect.",
            "SVar": "Named script variable or reusable sub-ability.", "Text": "Additional displayed card text.",
            "Loyalty": "Starting loyalty counters.", "AI": "AI deck-building directive.",
        }.items()
    ]
    for filename in guide_names:
        path = root / filename
        if not path.exists():
            continue
        sections = re.split(r"(?m)^#{2,3} (.+?)\s*$", path.read_text(encoding="utf-8"))
        for index in range(1, len(sections), 2):
            heading, body = sections[index].strip(), sections[index + 1]
            description = next((line.strip() for line in body.splitlines() if line.strip() and not line.startswith(("-", "*", "`", "#"))), "")
            required, optional = _parameters(body)
            example_match = re.search(r"`([^`\n]*(?:\$|:)[^`\n]*)`", body)
            for name in (part.strip() for part in heading.split("/")):
                if name and name.lower() not in {"parameters", "examples", "factories (in alphabetical order)"} and description:
                    records.append(DocumentationRecord(name, path.stem, description, tuple(required), tuple(optional), example_match.group(1) if example_match else None))
    return records


def _parameters(body: str) -> tuple[list[str], list[str]]:
    required: list[str] = []
    optional: list[str] = []
    for line in body.splitlines():
        match = re.match(r"\s*[-*]\s+`?([A-Za-z][\w]*\$?(?:/[\w$]+)*)`?[^\n]*", line)
        if match:
            (optional if re.search(r"optional|default", line, re.IGNORECASE) else required).append(match.group(1))
    return required, optional


def compile_pack(destination: Path, records: list[DocumentationRecord], content_version: str = "1") -> None:
    """Validate records and write a deterministic standalone SQLite pack."""
    seen: set[tuple[str, str]] = set()
    for record in records:
        key = (record.scope, record.name)
        if not record.name or not record.description:
            raise ValueError(f"Documentation entry '{record.name}' needs a description.")
        if key in seen:
            raise ValueError(f"Duplicate documentation entry: {record.scope}: {record.name}")
        seen.add(key)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".building")
    temporary.unlink(missing_ok=True)
    connection = sqlite3.connect(temporary)
    try:
        connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
        connection.execute("CREATE TABLE documentation (scope TEXT NOT NULL, name TEXT NOT NULL, category TEXT NOT NULL, description TEXT NOT NULL, parameters TEXT NOT NULL, optional_parameters TEXT NOT NULL, example TEXT NOT NULL, PRIMARY KEY(scope, name))")
        connection.execute("CREATE INDEX documentation_name ON documentation(name)")
        connection.executemany("INSERT INTO metadata VALUES (?, ?)", (("format", PACK_FORMAT), ("format_version", PACK_VERSION), ("content_version", content_version)))
        connection.executemany(
            "INSERT INTO documentation VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(item.scope, item.name, item.category, item.description, "\x1f".join(item.parameters), "\x1f".join(item.optional_parameters), item.example or "") for item in sorted(records, key=lambda item: (item.scope, item.name))],
        )
        connection.commit()
    finally:
        connection.close()
    temporary.replace(destination)
