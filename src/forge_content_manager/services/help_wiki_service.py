"""Load the bundled, searchable help wiki."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class HelpPage:
    """One page in the bundled help wiki."""

    group_id: str
    group_title: str
    slug: str
    title: str
    summary: str
    content: str

    @property
    def search_text(self) -> str:
        """Return the page fields used by the wiki search."""
        return f"{self.title}\n{self.summary}\n{self.content}".casefold()


@dataclass(frozen=True, slots=True)
class HelpGroup:
    """A named collection of related help pages."""

    group_id: str
    title: str
    pages: tuple[HelpPage, ...]


_FRONT_MATTER = re.compile(r"\A---\s*\n(?P<fields>.*?)\n---\s*\n(?P<body>.*)\Z", re.DOTALL)


def _display_name(value: str) -> str:
    """Turn a file or directory name into a readable title."""
    return value.replace("-", " ").replace("_", " ").strip().title()


def load_help_wiki(root: Path) -> tuple[HelpGroup, ...]:
    """Read every Markdown page below ``root`` and group pages by folder.

    Pages use a small optional front matter block with ``title`` and
    ``summary`` fields. Keeping parsing here means the UI only deals with
    ready-to-display page records and the content remains easy to author.
    """
    if not root.is_dir():
        return ()

    groups: list[HelpGroup] = []
    for directory in sorted((path for path in root.iterdir() if path.is_dir()), key=lambda path: path.name.casefold()):
        pages: list[HelpPage] = []
        for path in sorted(directory.glob("*.md"), key=lambda item: item.name.casefold()):
            pages.append(_load_page(path, directory))
        if pages:
            groups.append(HelpGroup(directory.name, _display_name(directory.name), tuple(pages)))
    return tuple(groups)


def _load_page(path: Path, group_directory: Path) -> HelpPage:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    title = _display_name(path.stem)
    summary = ""
    body = text
    match = _FRONT_MATTER.match(text)
    if match:
        body = match.group("body").strip()
        fields = {
            key.strip().casefold(): value.strip()
            for key, value in (line.split(":", maxsplit=1) for line in match.group("fields").splitlines() if ":" in line)
        }
        title = fields.get("title", title)
        summary = fields.get("summary", "")
    if not summary:
        summary = next((line.removeprefix("#").strip() for line in body.splitlines() if line.strip() and not line.startswith("#")), "")
    heading = next((line.removeprefix("#").strip() for line in body.splitlines() if line.startswith("# ")), "")
    if heading:
        title = heading
    return HelpPage(group_directory.name, _display_name(group_directory.name), path.stem, title, summary, body)


def default_help_root() -> Path:
    """Resolve help content from the source tree or a PyInstaller bundle."""
    bundle_root = getattr(sys, "_MEIPASS", None)
    if bundle_root:
        return Path(bundle_root) / "forge_content_manager" / "help_pages"
    return Path(__file__).resolve().parents[1] / "help_pages"
