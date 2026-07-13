"""Developer-only commands for mining and compiling script documentation."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from collections.abc import Callable

from forge_content_manager.services.documentation_pack import compile_pack, parse_legacy_guides, parse_markdown_catalog


PRESETS = {
    "keyword": r"(?m)^K:\s*([^|\r\n]+)",
    "ability-mode": r"(?m)^(?:A|SVar:[^:]+):(?:DB|SP|AB)\$\s*([^|\r\n]+)",
    "trigger-mode": r"(?m)^(?:T|SVar:[^:]+):Mode\$\s*([^|\r\n]+)",
    "static-mode": r"(?m)^S:Mode\$\s*([^|\r\n]+)",
    "replacement-mode": r"(?m)^R:Event\$\s*([^|\r\n]+)",
    "parameter": r"\|\s*([A-Za-z][\w]*\$)",
}


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


def terminal_progress(completed: int, total: int) -> None:
    """Render extraction progress without mixing status text into command output."""
    width = 30
    ratio = completed / total if total else 1
    filled = round(width * ratio)
    print(f"\rScanning {completed:,}/{total:,} files [{'#' * filled}{'.' * (width - filled)}] {ratio:.0%}", end="", file=sys.stderr, flush=True)
    if completed == total:
        print(file=sys.stderr)


def write_discoveries(destination: Path, terms: list[str], title: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"# {title}\n\n" + "\n\n".join(f"## `{term}`\n\nTODO: Write documentation." for term in terms) + ("\n" if terms else ""), encoding="utf-8")


def sync_catalog(discoveries: Path, catalog: Path) -> int:
    """Append missing discovery headings as editable stubs without touching entries."""
    found = re.findall(r"(?m)^##\s+`?(.+?)`?\s*$", discoveries.read_text(encoding="utf-8"))
    current = catalog.read_text(encoding="utf-8") if catalog.exists() else f"# {catalog.stem.replace('-', ' ').title()}\n"
    existing = {value.casefold() for value in re.findall(r"(?m)^##\s+`?(.+?)`?\s*$", current)}
    additions = [value for value in found if value.casefold() not in existing]
    if additions:
        catalog.parent.mkdir(parents=True, exist_ok=True)
        catalog.write_text(current.rstrip() + "\n\n" + "\n\n".join(f"## `{value}`\n\nTODO: Write documentation." for value in additions) + "\n", encoding="utf-8")
    return len(additions)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="forge-content-manager docs")
    commands = parser.add_subparsers(dest="command", required=True)
    extract = commands.add_parser("extract")
    extract.add_argument("--cards-dir", type=Path, required=True)
    extract.add_argument("--preset", choices=sorted(PRESETS))
    extract.add_argument("--pattern")
    extract.add_argument("--output", type=Path, required=True)
    extract.add_argument("--title", default="Discovered Forge Terms")
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
        print(f"Finding Forge scripts in {args.cards_dir}…", file=sys.stderr)
        terms = extract_terms(args.cards_dir, PRESETS.get(args.preset, args.pattern), terminal_progress)
        write_discoveries(args.output, terms, args.title)
        print(f"Wrote {len(terms):,} discovered terms to {args.output}", file=sys.stderr)
    elif args.command == "sync":
        print(f"Added {sync_catalog(args.discoveries, args.catalog)} documentation stubs.")
    else:
        records = parse_legacy_guides(args.guides_dir) if args.guides_dir else []
        authored = parse_markdown_catalog(args.catalog_dir)
        authored_names = {record.name.casefold() for record in authored}
        compile_pack(args.output, [record for record in records if record.name.casefold() not in authored_names] + authored, args.version)


if __name__ == "__main__":
    main()
