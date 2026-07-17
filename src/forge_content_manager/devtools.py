"""Developer-only commands for mining and compiling script documentation."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from queue import SimpleQueue
from threading import Lock
from typing import TypeVar

from forge_content_manager.services.documentation_pack import compile_pack, parse_legacy_guides, parse_markdown_catalog

# These regex patterns are used to extract terms from Forge text scripts. Each pattern must contain one capture group for the discovered term.
PRESETS = {
    "keyword": r"(?m)^K:\s*([^|\r\n]+)",
    "ability-mode": r"(?m)^(?:A|SVar:[^:]+):(?:DB|SP|AB)\$\s*([^|\r\n]+)",
    "trigger-mode": r"(?m)^(?:T|SVar:[^:]+):Mode\$\s*([^|\r\n]+)",
    "static-mode": r"(?m)^S:Mode\$\s*([^|\r\n]+)",
    "replacement-mode": r"(?m)^R:Event\$\s*([^|\r\n]+)",
    "parameter": r"\|\s*([A-Za-z][\w]*\$)",
}

# This maps the preset names to the scope that will be used in the generated documentation.
PRESET_SCOPES = {
    "keyword": "K",
    "ability-mode": "A",
    "trigger-mode": "T",
    "static-mode": "S",
    "replacement-mode": "R",
    "parameter": "*",
}

# These paramaters are expected to contain free-form text, so we don't attempt to enumerate their values.
FREE_TEXT_PARAMETERS = frozenset({"SpellDescription", "Description", "ValidDescription", "Name", "Execute", "SubAbility", "TriggerDescription", "StackDescription", "TgtPrompt"})

# These parameters can have many different values, but we only want to show a limited number of them in the documentation.
LIMITED_PARAMETERS = frozenset({"Cost", "ValidCard", "ValidCards", "Affected", "ValidTarget", "Spellbook", 
                                "ValidTargets", "ValidZone", "ChangeValid", "IsPresent", "ValidSource",
                                "AddAbility", "AddKeyword", "AddSVar", "AddTrigger", "AddType"
                                })
LIMIT_FOR_LIMITED_PARAMETERS = 10
ScanResult = TypeVar("ScanResult")


def scan_card_scripts(
    cards_dir: Path,
    extract: Callable[[str], ScanResult],
    progress: Callable[[int, int], None] | None = None,
) -> list[ScanResult | None]:
    """Read and extract every card script concurrently by top-level subdirectory.

    Results are collected in a thread-safe queue and restored to sorted path order
    before returning. This keeps discoveries deterministic while allowing the
    independent card-script directories to overlap filesystem reads and parsing.

    Args:
        cards_dir: Root directory containing Forge card-script text files.
        extract: Function that extracts one result from a readable script.
        progress: Optional callback receiving completed and total script counts.

    Returns:
        One result per script, in sorted path order; unreadable scripts are ``None``.
    """
    paths = sorted(cards_dir.rglob("*.txt"))
    total = len(paths)
    if progress:
        progress(0, total)
    if not paths:
        return []

    groups: dict[str, list[tuple[int, Path]]] = {}
    for index, path in enumerate(paths):
        relative_parts = path.relative_to(cards_dir).parts
        group_name = relative_parts[0] if len(relative_parts) > 1 else ""
        groups.setdefault(group_name, []).append((index, path))

    results: SimpleQueue[tuple[int, ScanResult | None]] = SimpleQueue()
    completed = 0
    progress_lock = Lock()

    def scan_group(group: list[tuple[int, Path]]) -> None:
        nonlocal completed
        for index, path in group:
            try:
                result = extract(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError):
                result = None
            results.put((index, result))
            if progress:
                with progress_lock:
                    completed += 1
                    progress(completed, total)

    max_workers = min(32, len(groups))
    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="halcyon-extract") as executor:
        futures = [executor.submit(scan_group, group) for group in groups.values()]
        for future in futures:
            future.result()

    return [result for _, result in sorted((results.get() for _ in paths), key=lambda item: item[0])]


def extract_terms(cards_dir: Path, pattern: str, progress: Callable[[int, int], None] | None = None) -> list[str]:
    """Return sorted, distinct first-capture matches from Forge text scripts."""
    expression = re.compile(pattern)
    if expression.groups < 1:
        raise ValueError("The extraction pattern must contain one capture group for the discovered term.")
    values: set[str] = set()
    for matches in scan_card_scripts(
        cards_dir,
        lambda text: {match.group(1).strip() for match in expression.finditer(text) if match.group(1).strip()},
        progress,
    ):
        if matches:
            values.update(matches)
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
    families: dict[str, KeywordFamily] = {}
    expression = re.compile(PRESETS["keyword"])

    def extract_keywords(text: str) -> list[tuple[str, list[str]]]:
        discoveries: list[tuple[str, list[str]]] = []
        for match in expression.finditer(text):
            parts = [part.strip() for part in match.group(1).split(":")]
            if not parts or not parts[0]:
                continue
            discoveries.append((parts[0], parts[1:]))

        return discoveries

    for discoveries in scan_card_scripts(cards_dir, extract_keywords, progress):
        if not discoveries:
            continue
        for title, values in discoveries:
            family = families.setdefault(title, KeywordFamily(title, []))
            while len(family.arguments) < len(values):
                family.arguments.append(set())
            for argument_index, value in enumerate(values):
                if value:
                    family.arguments[argument_index].add(value)
    return sorted(families.values(), key=lambda item: item.title.casefold())


def extract_ability_families(cards_dir: Path, scope: str, progress: Callable[[int, int], None] | None = None) -> list[AbilityFamily]:
    """Group mode declarations by family and retain their pipe-delimited values.

    ``SVar`` labels deliberately do not participate in the family key: an SVar is
    a local name, while the mode after ``DB$``, ``SP$``, ``AB$``, ``Mode$``, or
    ``Event$`` is the reusable Forge construct being documented.
    """
    if scope not in {"A", "T", "S", "R"}:
        raise ValueError("Mode families can only be extracted for A, T, S, or R scopes.")
    first_field = {"A": r"(?:DB|SP|AB)", "T": "Mode", "S": "Mode", "R": "Event"}[scope]
    prefix = rf"(?:{scope}|SVar:[^:\r\n]+)" if scope in {"A", "T"} else scope
    expression = re.compile(rf"(?m)^{prefix}:{first_field}\$\s*([^|\r\n]+)(.*)$")
    parameter_expression = re.compile(r"\|\s*([A-Za-z][\w]*)\$\s*([^|\r\n]*)")
    families: dict[str, AbilityFamily] = {}
    seen_parameters: dict[tuple[str, str], set[str]] = {}

    def extract_families(text: str) -> list[tuple[str, list[tuple[str, str]]]]:
        discoveries: list[tuple[str, list[tuple[str, str]]]] = []
        for match in expression.finditer(text):
            title = match.group(1).strip()
            if not title:
                continue
            parameters = [
                (parameter.group(1), parameter.group(2).strip())
                for parameter in parameter_expression.finditer(match.group(2))
            ]
            discoveries.append((title, parameters))

        return discoveries

    for discoveries in scan_card_scripts(cards_dir, extract_families, progress):
        if not discoveries:
            continue
        for title, parameters in discoveries:
            family = families.setdefault(title, AbilityFamily(title, {}))
            for label, value in parameters:
                observed = family.parameters.setdefault(label, [])
                seen = seen_parameters.setdefault((title, label), set())
                if value and value not in seen:
                    seen.add(value)
                    observed.append(value)
    return sorted(families.values(), key=lambda item: item.title.casefold())


def extract_ability_and_trigger_families(cards_dir: Path, progress: Callable[[int, int], None] | None = None) -> tuple[list[AbilityFamily], list[AbilityFamily]]:
    """Collect ability and trigger families in one pass over a card-script tree."""
    expressions = {
        "A": re.compile(r"(?m)^(?:A|SVar:[^:\r\n]+):(?:DB|SP|AB)\$\s*([^|\r\n]+)(.*)$"),
        "T": re.compile(r"(?m)^(?:T|SVar:[^:\r\n]+):Mode\$\s*([^|\r\n]+)(.*)$"),
    }
    parameter_expression = re.compile(r"\|\s*([A-Za-z][\w]*)\$\s*([^|\r\n]*)")
    families: dict[str, dict[str, AbilityFamily]] = {"A": {}, "T": {}}
    seen_parameters: dict[tuple[str, str, str], set[str]] = {}

    def extract_families(text: str) -> dict[str, list[tuple[str, list[tuple[str, str]]]]]:
        discoveries: dict[str, list[tuple[str, list[tuple[str, str]]]]] = {"A": [], "T": []}
        for scope, expression in expressions.items():
            for match in expression.finditer(text):
                title = match.group(1).strip()
                if not title:
                    continue
                parameters = [
                    (parameter.group(1), parameter.group(2).strip())
                    for parameter in parameter_expression.finditer(match.group(2))
                ]
                discoveries[scope].append((title, parameters))

        return discoveries

    for discoveries in scan_card_scripts(cards_dir, extract_families, progress):
        if not discoveries:
            continue
        for scope, scope_discoveries in discoveries.items():
            for title, parameters in scope_discoveries:
                family = families[scope].setdefault(title, AbilityFamily(title, {}))
                for label, value in parameters:
                    observed = family.parameters.setdefault(label, [])
                    seen = seen_parameters.setdefault((scope, title, label), set())
                    if value and value not in seen:
                        seen.add(value)
                        observed.append(value)
    return (
        sorted(families["A"].values(), key=lambda item: item.title.casefold()),
        sorted(families["T"].values(), key=lambda item: item.title.casefold()),
    )


def terminal_progress(completed: int, total: int) -> None:
    """Render extraction progress without mixing status text into command output."""
    if completed == 0:
        terminal_progress._last_percent = -1
    width = 30
    ratio = completed / total if total else 1
    percent = round(ratio * 100)
    if completed not in {0, total} and percent == getattr(terminal_progress, "_last_percent", -1):
        return
    terminal_progress._last_percent = percent
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
                    observed_values = values[:LIMIT_FOR_LIMITED_PARAMETERS] if label in LIMITED_PARAMETERS else sorted(values, key=str.casefold)
                    observed = ", ".join(f"`{value}`" for value in observed_values) or "_No values observed_"
                    lines.append(f"  Observed values: {observed}")
        entries.append("\n".join(lines))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"# {title}\n\n<!-- forge-doc-scope: {scope}: -->\n\n" + "\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")


def extract_preset(
    cards_dir: Path,
    preset: str,
    output: Path,
    progress: Callable[[int, int], None] | None = None,
) -> int:
    """Extract one bundled preset and write its discovery Markdown file."""
    if preset not in PRESETS:
        raise ValueError(f"Unknown extraction preset: {preset}")

    scope = PRESET_SCOPES[preset]
    title = "Discovered Forge Terms"
    if preset == "keyword":
        families = extract_keyword_families(cards_dir, progress)
        write_keyword_discoveries(output, families, title, scope)
        return len(families)
    if preset in {"ability-mode", "trigger-mode", "static-mode", "replacement-mode"}:
        families = extract_ability_families(cards_dir, scope, progress)
        write_ability_discoveries(output, families, title, scope)
        return len(families)

    terms = extract_terms(cards_dir, PRESETS[preset], progress)
    write_discoveries(output, terms, title, scope)
    return len(terms)


def refresh_documentation(
    cards_dir: Path,
    catalog_dir: Path,
    guides_dir: Path | None,
    output: Path,
    version: str = "2",
    progress: Callable[[int, int], None] | None = None,
) -> tuple[int, int]:
    """Regenerate A/T family catalogs and compile the editor documentation pack.

    Args:
        cards_dir: Recursive Forge card-script source directory.
        catalog_dir: Catalog directory whose ability and trigger files are replaced.
        guides_dir: Optional bundled legacy guide directory used as fallback data.
        output: SQLite documentation pack to create.
        version: Content version stored in the output pack.
        progress: Optional callback used while each source scan runs.

    Returns:
        The number of ability and trigger families written, in that order.

    Raises:
        OSError: If a source or output file cannot be read or written.
        ValueError: If the compiled records are incomplete or duplicate.
    """
    abilities, triggers = extract_ability_and_trigger_families(cards_dir, progress)
    write_ability_discoveries(catalog_dir / "ability-mode.md", abilities, "Ability Modes", "A")
    write_ability_discoveries(catalog_dir / "trigger-mode.md", triggers, "Trigger Modes", "T")
    
    records = parse_legacy_guides(guides_dir) if guides_dir else []
    authored = parse_markdown_catalog(catalog_dir)
    authored_keys = {(record.scope, record.name) for record in authored}
    compile_pack(output, [record for record in records if (record.scope, record.name) not in authored_keys] + authored, version)
    return len(abilities), len(triggers)


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
    parser = argparse.ArgumentParser(prog="halcyon docs")
    commands = parser.add_subparsers(dest="command", required=True)
    
    extract = commands.add_parser("extract")
    extract.add_argument("--cards-dir", type=Path, required=True)
    extract.add_argument("--preset", choices=sorted(PRESETS))
    extract.add_argument("--pattern")
    extract.add_argument("--output", type=Path, required=True)
    extract.add_argument("--title", default="Discovered Forge Terms")
    extract.add_argument("--scope", help="Documentation scope for a custom pattern, such as K or A.")

    extract_all = commands.add_parser("extract_all_presets", help="Extract every bundled preset into a directory of Markdown files.")
    extract_all.add_argument("--cards-dir", type=Path, required=True)
    extract_all.add_argument("--output-dir", type=Path, required=True)
    
    sync = commands.add_parser("sync")
    sync.add_argument("--discoveries", type=Path, required=True)
    sync.add_argument("--catalog", type=Path, required=True)
    
    compile_command = commands.add_parser("compile")
    compile_command.add_argument("--catalog-dir", type=Path, required=True)
    compile_command.add_argument("--guides-dir", type=Path)
    compile_command.add_argument("--output", type=Path, required=True)
    compile_command.add_argument("--version", default="1")
    
    refresh = commands.add_parser("refresh", help="Regenerate A/T catalogs and compile the documentation pack.")
    refresh.add_argument("--cards-dir", type=Path, required=True)
    refresh.add_argument("--catalog-dir", type=Path, default=Path("scripting_docs/catalog"))
    refresh.add_argument("--guides-dir", type=Path, default=Path("scripting_docs"))
    refresh.add_argument("--output", type=Path, default=Path("scripting_docs/script_documentation.sqlite3"))
    refresh.add_argument("--version", default="1")
    
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
        elif args.preset in {"ability-mode", "trigger-mode", "static-mode", "replacement-mode"}:
            families = extract_ability_families(args.cards_dir, scope, terminal_progress)
            write_ability_discoveries(args.output, families, args.title, scope)
            print(f"Wrote {len(families):,} {scope} families to {args.output}", file=sys.stderr)
        else:
            terms = extract_terms(args.cards_dir, PRESETS.get(args.preset, args.pattern), terminal_progress)
            write_discoveries(args.output, terms, args.title, scope)
            print(f"Wrote {len(terms):,} discovered terms to {args.output}", file=sys.stderr)
    elif args.command == "extract_all_presets":
        args.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Finding Forge scripts in {args.cards_dir}…", file=sys.stderr)
        for preset in PRESETS:
            output = args.output_dir / f"{preset}.md"
            count = extract_preset(args.cards_dir, preset, output, terminal_progress)
            print(f"Wrote {count:,} {preset} discoveries to {output}", file=sys.stderr)
    elif args.command == "sync":
        print(f"Added {sync_catalog(args.discoveries, args.catalog)} documentation stubs.")
    elif args.command == "refresh":
        print(f"Refreshing documentation from {args.cards_dir}…", file=sys.stderr)
        abilities, triggers = refresh_documentation(args.cards_dir, args.catalog_dir, args.guides_dir, args.output, args.version, terminal_progress)
        print(f"Wrote {abilities:,} ability families, {triggers:,} trigger families, and {args.output}.", file=sys.stderr)
    else:
        records = parse_legacy_guides(args.guides_dir) if args.guides_dir else []
        authored = parse_markdown_catalog(args.catalog_dir)
        authored_keys = {(record.scope, record.name) for record in authored}
        compile_pack(args.output, [record for record in records if (record.scope, record.name) not in authored_keys] + authored, args.version)


if __name__ == "__main__":
    main()
