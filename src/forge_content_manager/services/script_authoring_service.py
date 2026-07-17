"""Reference data and lightweight authoring helpers for Forge card scripts."""

from __future__ import annotations

import os
import re
import sqlite3
import sys
import threading
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path

from forge_content_manager.services.documentation_pack import LEGACY_GUIDE_NAMES, load_pack, parse_legacy_guides


# Parameter values that name local SVars. Extend this tuple when Forge adds
# another parameter with the same reference semantics.
SVAR_REFERENCE_PARAMETERS = ("Execute", "SubAbility", "Triggers", "ReplaceWith")
SVAR_REFERENCE_PARAMETER_PATTERN = "|".join(map(re.escape, SVAR_REFERENCE_PARAMETERS))


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
    script_id: int
    source_path: str


@dataclass(frozen=True, slots=True)
class SVarReference:
    """A local SVar reference and whether its target exists."""

    label: str
    value: str
    line_number: int
    start: int
    end: int


class ScriptAuthoringService:
    """Loads bundled Forge documentation and optional reference-card scripts."""

    _GUIDE_NAMES = LEGACY_GUIDE_NAMES

    def __init__(self, reference_cards_dir: Path | None = None, database_path: Path | None = None, documentation_path: Path | None = None) -> None:
        """Initialize documentation lookup and optional reference indexing.

        Args:
            reference_cards_dir: Optional Forge ``cardsfolder`` source directory.
            database_path: SQLite path used for the searchable reference index.
            documentation_path: Optional compiled documentation pack path.
        """
        self._reference_cards_dir = reference_cards_dir or self._bundled_reference_directory()
        self._database_path = database_path or Path.home() / ".forge_content_manager_reference_cards.sqlite3"
        self._documentation_path = documentation_path or self._bundled_documentation_path()
        self._catalog = self._load_catalog()
        self._state_lock = threading.Lock()
        self._indexing = False
        self._pending_reindex = False
        self._index_error: str | None = None
        self._ready = self._database_matches_reference()
        if self._reference_directory_available() and not self._ready:
            self.start_indexing()

    @property
    def reference_cards_dir(self) -> Path | None:
        """Return the configured optional cardsfolder directory."""
        return self._reference_cards_dir

    def set_reference_cards_dir(self, directory: Path | None) -> None:
        """Change the reference source and build its SQLite index in the background."""
        self._reference_cards_dir = directory
        self._ready = self._database_matches_reference()
        self._index_error = None
        if self._reference_directory_available() and not self._ready:
            self.start_indexing()

    def set_documentation_path(self, path: Path | None) -> None:
        """Reload documentation from a bundled or user-installed pack."""
        self._documentation_path = path or self._bundled_documentation_path()
        self._catalog = self._load_catalog()

    def start_indexing(self) -> bool:
        """Start a background rebuild when a valid source folder is configured."""
        if not self._reference_directory_available():
            return False
        with self._state_lock:
            if self._indexing:
                self._pending_reindex = True
                return False
            self._indexing = True
            self._ready = False
            self._index_error = None
        directory = self._reference_cards_dir
        threading.Thread(target=self._build_index, args=(directory,), name="Forge reference index", daemon=True).start()
        return True

    def wait_until_ready(self, timeout: float = 10) -> bool:
        """Wait for a background index only when callers explicitly need to do so."""
        import time

        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            with self._state_lock:
                if not self._indexing:
                    return self._ready
            time.sleep(0.01)
        return False

    @property
    def is_indexing(self) -> bool:
        """Report whether a background database rebuild is currently running."""
        with self._state_lock:
            return self._indexing

    def complete(self, prefix: str, limit: int = 20, scope: str | None = None) -> list[ScriptDocumentation]:
        """Return case-insensitive documentation matches for a token prefix."""
        needle = prefix.strip().casefold()
        if scope is None:
            values = list(self._catalog.values())
        elif scope == "*":
            values = [item for (item_scope, _name), item in self._catalog.items() if item_scope == "*"]
        else:
            # Family-specific records are authoritative.  The global parameter
            # catalog fills only names that have not been documented for the
            # active family, preventing duplicate and misleading suggestions.
            values_by_name: dict[str, ScriptDocumentation] = {
                name: item for (item_scope, name), item in self._catalog.items() if item_scope == scope
            }
            for (item_scope, name), item in self._catalog.items():
                if item_scope == "*":
                    values_by_name.setdefault(name, item)
            values = list(values_by_name.values())
        matches = [item for item in values if not needle or item.name.casefold().startswith(needle)]
        matches.sort(key=lambda item: (not item.name.casefold().startswith(needle), item.name.casefold()))
        return matches[:limit]

    def complete_context(self, line: str, cursor: int, prefix: str, limit: int = 20) -> list[ScriptDocumentation]:
        """Return completion choices appropriate to a mode, parameter, or value slot."""
        scope = self.scope_for_line(line)
        family = self.family_for_line(line)
        parameter = self._parameter_at(line, cursor)
        if family and parameter:
            record = self.lookup(parameter, f"{scope}:{family}")
            if record is not None:
                return [
                    ScriptDocumentation(value, f"Observed {parameter} value", record.description)
                    for value in record.parameters
                    if not prefix or value.casefold().startswith(prefix.strip().casefold())
                ][:limit]
        if family and self._typing_parameter_label(line, cursor):
            return self.complete(prefix, limit, f"{scope}:{family}")
        return self.complete(prefix, limit, scope)

    def lookup(self, token: str, scope: str | None = None) -> ScriptDocumentation | None:
        """Find documentation for an exact, case-sensitive term in the relevant scope."""
        name = token.strip()
        if scope is not None:
            return self._catalog.get((scope, name)) or (self._catalog.get(("*", name)) if scope != "*" else None)
        matches = [item for (item_scope, item_name), item in self._catalog.items() if item_name == name]
        if len(matches) == 1:
            return matches[0]
        return self._catalog.get(("*", name)) or self._catalog.get(("K", f"K:{name}"))

    def lookup_context(self, line: str, cursor: int) -> ScriptDocumentation | None:
        """Resolve the most specific Forge expression containing the caret."""
        scope = self.scope_for_line(line)
        family = self.family_for_line(line)
        candidates: list[str] = []
        for match in re.finditer(r"\b([A-Za-z][\w]*)\$\s*([^|\r\n]+)", line):
            if match.start() <= cursor <= match.end():
                key, value = match.group(1), match.group(2).strip()
                if family and (item := self.lookup(f"{key}$", f"{scope}:{family}")) is not None:
                    return item
                candidates.extend((f"{key}$ {value}", value, f"{key}$"))
        for match in re.finditer(r"(?:^|\s)K:\s*([^|\r\n]+)", line):
            if match.start() <= cursor <= match.end():
                value = match.group(1).strip()
                candidates.extend((f"K:{value}", value, *self._keyword_templates(value), "K"))
        word = self._current_word(line, cursor)
        if word:
            candidates.append(word)
        return next((item for candidate in candidates if (item := self.lookup(candidate, scope)) is not None), None)

    @staticmethod
    def scope_for_line(line: str) -> str:
        """Determine the relevant documentation category from a Forge script line."""
        match = re.match(r"\s*(K|A|T|S|R|SVar):", line)
        if match is None:
            return "*"
        prefix = match.group(1)
        if prefix == "SVar":
            first_field = re.match(r"\s*SVar:[^:]+:(DB|SP|AB|Mode)\$", line)
            if first_field is not None:
                return "T" if first_field.group(1) == "Mode" else "A"
            return "SVar"
        return prefix

    @staticmethod
    def family_for_line(line: str) -> str | None:
        """Return the mode family declared by an A, T, S, or R line."""
        scope = ScriptAuthoringService.scope_for_line(line)
        if scope == "A":
            match = re.match(r"\s*(?:A|SVar:[^:]+):(?:DB|SP|AB)\$\s*([^|\r\n]+)", line)
        elif scope == "T":
            match = re.match(r"\s*(?:T|SVar:[^:]+):Mode\$\s*([^|\r\n]+)", line)
        elif scope == "S":
            match = re.match(r"\s*S:Mode\$\s*([^|\r\n]+)", line)
        elif scope == "R":
            match = re.match(r"\s*R:Event\$\s*([^|\r\n]+)", line)
        else:
            return None
        return match.group(1).strip() if match and match.group(1).strip() else None

    @staticmethod
    def unresolved_svar_references(text: str) -> list[SVarReference]:
        """Find configured SVar-reference values not declared by an SVar line."""
        declared = {match.group(1) for match in re.finditer(r"(?m)^\s*SVar:([^:\r\n]+):", text)}
        unresolved: list[SVarReference] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in re.finditer(rf"\|\s*({SVAR_REFERENCE_PARAMETER_PATTERN})\$\s*([^|\r\n]+)", line):
                value = match.group(2).strip()
                if value and value not in declared:
                    start = match.start(2) + len(match.group(2)) - len(match.group(2).lstrip())
                    unresolved.append(SVarReference(match.group(1), value, line_number, start, start + len(value)))
        return unresolved

    @staticmethod
    def _parameter_at(line: str, cursor: int) -> str | None:
        for match in re.finditer(r"\|\s*([A-Za-z][\w]*)\$\s*([^|\r\n]*)", line):
            if match.start(2) <= cursor <= match.end(2):
                return f"{match.group(1)}$"
        return None

    @staticmethod
    def _typing_parameter_label(line: str, cursor: int) -> bool:
        before = line[:cursor]
        return bool(re.search(r"\|\s*[A-Za-z][\w]*$", before))

    def search_reference_cards(self, query: str, limit: int = 100) -> list[ReferenceCard]:
        """Search optional reference scripts by display name."""
        needle = query.strip().casefold()
        with self._state_lock:
            ready = self._ready
        if not ready:
            return []
        connection = sqlite3.connect(self._database_path)
        try:
            rows = connection.execute(
                "SELECT id, name, source_path FROM cards WHERE name LIKE ? COLLATE NOCASE ORDER BY name LIMIT ?",
                (f"%{needle}%", limit),
            ).fetchall()
        finally:
            connection.close()
        return [ReferenceCard(name=row[1], script_id=row[0], source_path=row[2]) for row in rows]

    def load_reference_card(self, card: ReferenceCard) -> str:
        """Load a reference script exactly as UTF-8 text."""
        connection = sqlite3.connect(self._database_path)
        try:
            row = connection.execute("SELECT script_text FROM cards WHERE id = ?", (card.script_id,)).fetchone()
        finally:
            connection.close()
        if row is None:
            raise ValueError("The selected reference script is no longer in the index.")
        return row[0]

    def reference_status(self) -> str:
        """Return a concise user-facing reference-library state."""
        with self._state_lock:
            indexing, ready, error = self._indexing, self._ready, self._index_error
        if indexing:
            return "Building reference database… searches will be available when indexing finishes."
        if error:
            return f"Reference database failed: {error}"
        if ready:
            return "Reference database ready."
        return "Reference library unavailable. Choose a Forge cardsfolder in Settings."

    def _reference_directory_available(self) -> bool:
        return self._reference_cards_dir is not None and self._reference_cards_dir.is_dir()

    def _database_matches_reference(self) -> bool:
        if not self._reference_directory_available() or not self._database_path.exists():
            return False
        try:
            connection = sqlite3.connect(self._database_path)
            try:
                row = connection.execute("SELECT value FROM metadata WHERE key = 'source_dir'").fetchone()
            finally:
                connection.close()
            return row is not None and row[0] == str(self._reference_cards_dir.resolve())
        except sqlite3.Error:
            return False

    def _build_index(self, source_directory: Path) -> None:
        """Recursively store source scripts in a replacement SQLite database."""
        temporary_path = self._database_path.with_suffix(".building.sqlite3")
        try:
            self._database_path.parent.mkdir(parents=True, exist_ok=True)
            temporary_path.unlink(missing_ok=True)
            connection = sqlite3.connect(temporary_path)
            try:
                connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
                connection.execute("CREATE TABLE cards (id INTEGER PRIMARY KEY, name TEXT NOT NULL, source_path TEXT NOT NULL, script_text TEXT NOT NULL)")
                connection.execute("CREATE INDEX cards_name_index ON cards(name COLLATE NOCASE)")
                connection.execute("INSERT INTO metadata(key, value) VALUES ('source_dir', ?)", (str(source_directory.resolve()),))
                for path in source_directory.rglob("*.txt"):
                    try:
                        script_text = path.read_text(encoding="utf-8")
                    except (OSError, UnicodeError):
                        continue
                    first_line = script_text.splitlines()[0] if script_text else ""
                    name = first_line.removeprefix("Name:").strip() if first_line.startswith("Name:") else path.stem
                    connection.execute(
                        "INSERT INTO cards(name, source_path, script_text) VALUES (?, ?, ?)",
                        (name, str(path), script_text),
                    )
                connection.commit()
            finally:
                connection.close()
            os.replace(temporary_path, self._database_path)
            with self._state_lock:
                self._ready = True
        except (OSError, sqlite3.Error) as exc:
            with suppress(OSError):
                temporary_path.unlink(missing_ok=True)
            with self._state_lock:
                self._index_error = str(exc)
                self._ready = False
        finally:
            with self._state_lock:
                self._indexing = False
                restart = self._pending_reindex
                self._pending_reindex = False
            if restart:
                self.start_indexing()

    def _load_catalog(self) -> dict[str, ScriptDocumentation]:
        catalog: dict[tuple[str, str], ScriptDocumentation] = {}
        try:
            records = load_pack(self._documentation_path)
        except ValueError:
            root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3])) / "scripting_docs"
            records = parse_legacy_guides(root)
        for record in records:
            self._add(catalog, record.scope, ScriptDocumentation(record.name, record.category, record.description, record.parameters, record.optional_parameters, record.example))
        return catalog

    @staticmethod
    def _current_word(line: str, cursor: int) -> str:
        for match in re.finditer(r"[A-Za-z][\w]*", line):
            if match.start() <= cursor <= match.end():
                return match.group()
        return ""

    @staticmethod
    def _keyword_templates(value: str) -> list[str]:
        """Return authored family-template names for a concrete colon-delimited keyword."""
        parts = value.split(":")
        if len(parts) < 2 or not parts[0]:
            return []
        placeholders = ["<Selector>", "[<Label>]", *[f"[<Argument {index}>]" for index in range(3, len(parts))]]
        return [":".join([parts[0], *placeholders])]

    def _guide_paths(self) -> list[Path]:
        root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3]))
        return [root / "scripting_docs" / name for name in self._GUIDE_NAMES]

    @staticmethod
    def _bundled_reference_directory() -> Path | None:
        root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3]))
        directory = root / "scripting_docs" / "cards" / "cardsfolder"
        return directory if directory.is_dir() else None

    @staticmethod
    def _bundled_documentation_path() -> Path:
        root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[3]))
        return root / "scripting_docs" / "script_documentation.sqlite3"

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
    def _add(catalog: dict[tuple[str, str], ScriptDocumentation], scope: str, item: ScriptDocumentation) -> None:
        catalog.setdefault((scope, item.name), item)
