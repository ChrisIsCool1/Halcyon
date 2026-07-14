"""Developer-only commands for mining and compiling script documentation."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from forge_content_manager.services.documentation_pack import compile_pack, parse_legacy_guides, parse_markdown_catalog


PRESETS = {
    "keyword": r"(?m)^K:\s*([^|\r\n]+)",
    "ability-mode": r"(?m)^(?:A|SVar:[^:]+):(?:DB|SP|AB)\$\s*([^|\r\n]+)",
    "trigger-mode": r"(?m)^(?:T|SVar:[^:]+):Mode\$\s*([^|\r\n]+)",
    "static-mode": r"(?m)^S:Mode\$\s*([^|\r\n]+)",
    "replacement-mode": r"(?m)^R:Event\$\s*([^|\r\n]+)",
    "parameter": r"\|\s*([A-Za-z][\w]*\$)",
}
PRESET_SCOPES = {
    "keyword": "K",
    "ability-mode": "A",
    "trigger-mode": "T",
    "static-mode": "S",
    "replacement-mode": "R",
    "parameter": "*",
}

FREE_TEXT_PARAMETERS = frozenset({"SpellDescription", "TriggerDescription", "StackDescription", "TgtPrompt"})
MAX_COST_OBSERVED_VALUES = 10


def extract_terms(cards_dir: Path, pattern: str, progress: Callable[[int, int], None] | None = None) -> list[str]:
    """Return sorted, distinct first-capture matches from Forge text scripts."""
    expression = re.compile(pattern)
    if expression.groups < 1:
        raise ValueError("The extraction pattern must contain one capture group for the discovered term.")
    paths = list(cards_dir.rglob("*.txt"))
    total = len(paths)
    values: set[str] = set()
    if progress:
        progress(0, total)
    for index, path in enumerate(paths, start=1):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            pass
        else:
            values.update(match.group(1).strip() for match in expression.finditer(text) if match.group(1).strip())
        if progress:
            progress(index, total)
    return sorted(values, key=str.casefold)


@dataclass(slots=True)
class KeywordFamily:
    """A keyword title and the concrete values seen in each colon-delimited slot."""

    title: str
    arguments: list[set[str]]


@dataclass(slots=True)
class AbilityFamily:
    """One ability or trigger mode and the parameter values seen with it."""

    title: str
    parameters: dict[str, list[str]]


def extract_keyword_families(cards_dir: Path, progress: Callable[[int, int], None] | None = None) -> list[KeywordFamily]:
    """Group K declarations by title while retaining every observed argument value."""
    paths = list(cards_dir.rglob("*.txt"))
    families: dict[str, KeywordFamily] = {}
    if progress:
        progress(0, len(paths))
    for index, path in enumerate(paths, start=1):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            text = ""
        for match in re.finditer(PRESETS["keyword"], text):
            parts = [part.strip() for part in match.group(1).split(":")]
            if not parts or not parts[0]:
                continue
            title, values = parts[0], parts[1:]
            family = families.setdefault(title, KeywordFamily(title, []))
            while len(family.arguments) < len(values):
                family.arguments.append(set())
            for argument_index, value in enumerate(values):
                if value:
                    family.arguments[argument_index].add(value)
        if progress:
            progress(index, len(paths))
    return sorted(families.values(), key=lambda item: item.title.casefold())


def extract_ability_families(cards_dir: Path, scope: str, progress: Callable[[int, int], None] | None = None) -> list[AbilityFamily]:
    """Group A or T declarations by mode and retain their pipe-delimited values.

    ``SVar`` labels deliberately do not participate in the family key: an SVar is
    a local name, while the mode after ``DB$``, ``SP$``, ``AB$``, or ``Mode$`` is
    the reusable Forge construct being documented.
    """
    if scope not in {"A", "T"}:
        raise ValueError("Ability families can only be extracted for A or T scopes.")
    first_field = r"(?:DB|SP|AB)" if scope == "A" else "Mode"
    expression = re.compile(rf"(?m)^(?:{scope}|SVar:[^:\r\n]+):{first_field}\$\s*([^|\r\n]+)(.*)$")
    parameter_expression = re.compile(r"\|\s*([A-Za-z][\w]*)\$\s*([^|\r\n]*)")
    paths = list(cards_dir.rglob("*.txt"))
    families: dict[str, AbilityFamily] = {}
    if progress:
        progress(0, len(paths))
    for index, path in enumerate(paths, start=1):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            text = ""
        for match in expression.finditer(text):
            title = match.group(1).strip()
            if not title:
                continue
            family = families.setdefault(title, AbilityFamily(title, {}))
            for parameter in parameter_expression.finditer(match.group(2)):
                label, value = parameter.group(1), parameter.group(2).strip()
                observed = family.parameters.setdefault(label, [])
                if value and value not in observed:
                    observed.append(value)
        if progress:
            progress(index, len(paths))
    return sorted(families.values(), key=lambda item: item.title.casefold())


def terminal_progress(completed: int, total: int) -> None:
    """Render extraction progress without mixing status text into command output."""
    width = 30
    ratio = completed / total if total else 1
    filled = round(width * ratio)
    print(f"\rScanning {completed:,}/{total:,} files [{'#' * filled}{'.' * (width - filled)}] {ratio:.0%}", end="", file=sys.stderr, flush=True)
    if completed == total:
        print(file=sys.stderr)


def write_discoveries(destination: Path, terms: list[str], title: str, scope: str = "*") -> None:
    """Write placeholder Markdown entries for terms found during extraction.

    Args:
        destination: Markdown file to create or replace.
        terms: Discovered names that need authored documentation.
        title: Heading written at the top of the file.
        scope: Forge script prefix associated with the entries.

    Raises:
        OSError: If the destination cannot be created or written.
    """
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"# {title}\n\n<!-- forge-doc-scope: {scope}: -->\n\n" + "\n\n".join(f"## `{term}`\n\nTODO: Write documentation." for term in terms) + ("\n" if terms else ""), encoding="utf-8")


def write_keyword_discoveries(destination: Path, families: list[KeywordFamily], title: str, scope: str = "K") -> None:
    """Write one editable Markdown entry per keyword family and its argument slots."""
    entries: list[str] = []
    for family in families:
        placeholders = ["<Selector>", "[<Label>]", *[f"[<Argument {index}>]" for index in range(3, len(family.arguments) + 1)]]
        signature = ":".join([family.title, *placeholders[:len(family.arguments)]])
        lines = [f"## `{signature}`", "", "TODO: Write documentation."]
        if family.arguments:
            lines.extend(("", "**Arguments:**"))
            for index, values in enumerate(family.arguments, start=1):
                label = "Selector" if index == 1 else "Label (optional)" if index == 2 else f"Argument {index} (optional)"
                observed = ", ".join(f"`{value}`" for value in sorted(values, key=str.casefold)) or "_No values observed_"
                lines.extend((f"- **{label}:** TODO: Describe this argument.", f"  Observed values: {observed}"))
        entries.append("\n".join(lines))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"# {title}\n\n<!-- forge-doc-scope: {scope}: -->\n\n" + "\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")


def write_ability_discoveries(destination: Path, families: list[AbilityFamily], title: str, scope: str) -> None:
    """Write editable documentation entries for ability/trigger mode families."""
    entries: list[str] = []
    for family in families:
        lines = [f"## `{family.title}`", "", "TODO: Write documentation."]
        if family.parameters:
            lines.extend(("", "**Parameters:**"))
            for label, values in sorted(family.parameters.items(), key=lambda item: item[0].casefold()):
                lines.append(f"- `{label}$`: TODO: Describe this parameter.")
                if label not in FREE_TEXT_PARAMETERS:
                    observed_values = values[:MAX_COST_OBSERVED_VALUES] if label == "Cost" else sorted(values, key=str.casefold)
                    observed = ", ".join(f"`{value}`" for value in observed_values) or "_No values observed_"
                    lines.append(f"  Observed values: {observed}")
        entries.append("\n".join(lines))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"# {title}\n\n<!-- forge-doc-scope: {scope}: -->\n\n" + "\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")


def sync_catalog(discoveries: Path, catalog: Path) -> int:
    """Append complete missing discovery entries without touching authored entries."""
    source = discoveries.read_text(encoding="utf-8")
    source_scope_match = re.search(r"(?mi)^<!--\s*forge-doc-scope:\s*([A-Za-z]+):?\s*-->\s*$", source)
    source_scope = source_scope_match.group(1) if source_scope_match else "*"
    sections = re.split(r"(?m)^##\s+`?(.+?)`?\s*$", source)
    found = [(sections[index].strip(), sections[index + 1].strip()) for index in range(1, len(sections), 2)]
    current = catalog.read_text(encoding="utf-8") if catalog.exists() else f"# {catalog.stem.replace('-', ' ').title()}\n"
    catalog_scope_match = re.search(r"(?mi)^<!--\s*forge-doc-scope:\s*([A-Za-z]+):?\s*-->\s*$", current)
    if catalog_scope_match and catalog_scope_match.group(1) != source_scope:
        raise ValueError(f"Catalog scope {catalog_scope_match.group(1)} does not match discovery scope {source_scope}.")
    if not catalog_scope_match and source_scope != "*":
        current = re.sub(r"(?m)^(# .+\n)", rf"\1\n<!-- forge-doc-scope: {source_scope}: -->\n", current, count=1)
    existing = set(re.findall(r"(?m)^##\s+`?(.+?)`?\s*$", current))
    additions = [(name, body) for name, body in found if name not in existing]
    if additions:
        catalog.parent.mkdir(parents=True, exist_ok=True)
        catalog.write_text(current.rstrip() + "\n\n" + "\n\n".join(f"## `{name}`\n\n{body}" for name, body in additions) + "\n", encoding="utf-8")
    return len(additions)


def main(argv: list[str] | None = None) -> None:
    """Run the documentation discovery command-line interface.

    Args:
        argv: Optional argument vector; when omitted, uses ``sys.argv``.

    Raises:
        SystemExit: If argument parsing fails or a command reports an error.
        ValueError: If a discovery pattern or catalog has an invalid scope.
    """
    parser = argparse.ArgumentParser(prog="forge-content-manager docs")
    commands = parser.add_subparsers(dest="command", required=True)
    extract = commands.add_parser("extract")
    extract.add_argument("--cards-dir", type=Path, required=True)
    extract.add_argument("--preset", choices=sorted(PRESETS))
    extract.add_argument("--pattern")
    extract.add_argument("--output", type=Path, required=True)
    extract.add_argument("--title", default="Discovered Forge Terms")
    extract.add_argument("--scope", help="Documentation scope for a custom pattern, such as K or A.")
    sync = commands.add_parser("sync")
    sync.add_argument("--discoveries", type=Path, required=True)
    sync.add_argument("--catalog", type=Path, required=True)
    compile_command = commands.add_parser("compile")
    compile_command.add_argument("--catalog-dir", type=Path, required=True)
    compile_command.add_argument("--guides-dir", type=Path)
    compile_command.add_argument("--output", type=Path, required=True)
    compile_command.add_argument("--version", default="1")
    args = parser.parse_args(argv)
    if args.command == "extract":
        if bool(args.preset) == bool(args.pattern):
            parser.error("choose exactly one of --preset or --pattern")
        scope = PRESET_SCOPES.get(args.preset, args.scope or "*").removesuffix(":")
        print(f"Finding Forge scripts in {args.cards_dir}…", file=sys.stderr)
        if args.preset == "keyword":
            families = extract_keyword_families(args.cards_dir, terminal_progress)
            write_keyword_discoveries(args.output, families, args.title, scope)
            print(f"Wrote {len(families):,} keyword families to {args.output}", file=sys.stderr)
        elif args.preset in {"ability-mode", "trigger-mode"}:
            families = extract_ability_families(args.cards_dir, scope, terminal_progress)
            write_ability_discoveries(args.output, families, args.title, scope)
            print(f"Wrote {len(families):,} {scope} families to {args.output}", file=sys.stderr)
        else:
            terms = extract_terms(args.cards_dir, PRESETS.get(args.preset, args.pattern), terminal_progress)
            write_discoveries(args.output, terms, args.title, scope)
            print(f"Wrote {len(terms):,} discovered terms to {args.output}", file=sys.stderr)
    elif args.command == "sync":
        print(f"Added {sync_catalog(args.discoveries, args.catalog)} documentation stubs.")
    else:
        records = parse_legacy_guides(args.guides_dir) if args.guides_dir else []
        authored = parse_markdown_catalog(args.catalog_dir)
        authored_keys = {(record.scope, record.name) for record in authored}
        compile_pack(args.output, [record for record in records if (record.scope, record.name) not in authored_keys] + authored, args.version)


if __name__ == "__main__":
    main()
