"""Reference data and lightweight authoring helpers for Forge card scripts."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ScriptDocumentation:
    """Intellisense-style help for one Forge scripting term."""

    name: str
    category: str
    description: str
    parameters: tuple[str, ...] = ()
    optional_parameters: tuple[str, ...] = ()
    example: str | None = None

    @property
    def signature(self) -> str:
        """Return a compact display signature."""
        parameters = list(self.parameters) + [f"[{value}]" for value in self.optional_parameters]
        return f"{self.name} | " + " | ".join(parameters) if parameters else self.name


@dataclass(frozen=True, slots=True)
class ReferenceCard:
    """A searchable script from an optional Forge cardsfolder."""

    name: str
    path: Path


class ScriptAuthoringService:
    """Loads bundled Forge documentation and optional reference-card scripts."""

    _GUIDE_NAMES = (
        "Card-scripting-API.md",
        "AbilityFactory.md",
        "Triggers.md",
        "Targeting.md",
        "Statics.md",
        "Replacements.md",
        "Costs.md",
    )
    _METADATA = {
        "Name": "Card display name.", "ManaCost": "Mana cost shown in mana shards.",
        "Types": "Space-separated card types and subtypes.", "PT": "Power and toughness.",
        "Oracle": "Oracle text displayed by Forge.", "Colors": "Color indicator for cards without a mana cost.",
        "K": "Keyword ability; use one K: line per keyword.", "A": "Spell or activated ability.",
        "T": "Triggered ability.", "S": "Static ability.", "R": "Replacement effect.",
        "SVar": "Named script variable or reusable sub-ability.", "Text": "Additional displayed card text.",
        "Loyalty": "Starting loyalty counters.", "AI": "AI deck-building directive.",
    }

    def __init__(self, reference_cards_dir: Path | None = None) -> None:
        self._reference_cards_dir = reference_cards_dir or self._bundled_reference_directory()
        self._catalog = self._load_catalog()
        self._reference_cards: list[ReferenceCard] | None = None

    @property
    def reference_cards_dir(self) -> Path | None:
        """Return the configured optional cardsfolder directory."""
        return self._reference_cards_dir

    def set_reference_cards_dir(self, directory: Path | None) -> None:
        """Change the optional reference directory and discard its index."""
        self._reference_cards_dir = directory
        self._reference_cards = None

    def complete(self, prefix: str, limit: int = 20) -> list[ScriptDocumentation]:
        """Return case-insensitive documentation matches for a token prefix."""
        needle = prefix.strip().casefold()
        values = self._catalog.values()
        matches = [item for item in values if not needle or item.name.casefold().startswith(needle)]
        matches.sort(key=lambda item: (not item.name.casefold().startswith(needle), item.name.casefold()))
        return matches[:limit]

    def lookup(self, token: str) -> ScriptDocumentation | None:
        """Find documentation for an exact scripting token."""
        return self._catalog.get(token.strip().casefold())

    def search_reference_cards(self, query: str, limit: int = 100) -> list[ReferenceCard]:
        """Search optional reference scripts by display name."""
        needle = query.strip().casefold()
        if not self._reference_directory_available():
            return []
        if self._reference_cards is None:
            self._reference_cards = self._index_reference_cards()
        return [card for card in self._reference_cards if needle in card.name.casefold()][:limit]

    def load_reference_card(self, card: ReferenceCard) -> str:
        """Load a reference script exactly as UTF-8 text."""
        return card.path.read_text(encoding="utf-8")

    def reference_status(self) -> str:
        """Return a concise user-facing reference-library state."""
        if self._reference_directory_available():
            return f"Reference library: {self._reference_cards_dir}"
        return "Reference library unavailable. Choose a Forge cardsfolder in Settings."

    def _reference_directory_available(self) -> bool:
        return self._reference_cards_dir is not None and self._reference_cards_dir.is_dir()

    def _index_reference_cards(self) -> list[ReferenceCard]:
        assert self._reference_cards_dir is not None
        cards: list[ReferenceCard] = []
        for path in self._reference_cards_dir.rglob("*.txt"):
            try:
                first_line = path.read_text(encoding="utf-8").splitlines()[0]
            except (OSError, UnicodeError, IndexError):
                continue
            name = first_line.removeprefix("Name:").strip() if first_line.startswith("Name:") else path.stem
            cards.append(ReferenceCard(name=name, path=path))
        return sorted(cards, key=lambda card: card.name.casefold())

    def _load_catalog(self) -> dict[str, ScriptDocumentation]:
        catalog: dict[str, ScriptDocumentation] = {}
        for name, description in self._METADATA.items():
            self._add(catalog, ScriptDocumentation(name, "Card property", description))
        for path in self._guide_paths():
            if path.exists():
                self._parse_guide(path.read_text(encoding="utf-8"), path.stem, catalog)
        return catalog

    def _guide_paths(self) -> list[Path]:
        root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3]))
        return [root / "scripting_docs" / name for name in self._GUIDE_NAMES]

    @staticmethod
    def _bundled_reference_directory() -> Path | None:
        root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3]))
        directory = root / "scripting_docs" / "cards" / "cardsfolder"
        return directory if directory.is_dir() else None

    def _parse_guide(self, text: str, category: str, catalog: dict[str, ScriptDocumentation]) -> None:
        sections = re.split(r"(?m)^#{2,3} (.+?)\s*$", text)
        for index in range(1, len(sections), 2):
            raw_name, body = sections[index].strip(), sections[index + 1]
            for name in (part.strip() for part in raw_name.split("/")):
                if not name or name.lower() in {"parameters", "examples", "factories (in alphabetical order)"}:
                    continue
                description = next((line.strip() for line in body.splitlines() if line.strip() and not line.startswith(("-", "*", "`", "#"))), "" )
                required, optional = self._parameters(body)
                example_match = re.search(r"`([^`\n]*(?:\$|:)[^`\n]*)`", body)
                self._add(catalog, ScriptDocumentation(name, category, description, tuple(required), tuple(optional), example_match.group(1) if example_match else None))

    @staticmethod
    def _parameters(body: str) -> tuple[list[str], list[str]]:
        required: list[str] = []
        optional: list[str] = []
        for line in body.splitlines():
            match = re.match(r"\s*[-*]\s+`?([A-Za-z][\w]*\$?(?:/[\w$]+)*)`?[^\n]*", line)
            if not match:
                continue
            target = optional if re.search(r"optional|default", line, re.IGNORECASE) else required
            target.append(match.group(1))
        return required, optional

    @staticmethod
    def _add(catalog: dict[str, ScriptDocumentation], item: ScriptDocumentation) -> None:
        catalog.setdefault(item.name.casefold(), item)
