"""Tests for the bundled help wiki loader and search-oriented page model."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from forge_content_manager.services.help_wiki_service import load_help_wiki


class HelpWikiServiceTests(unittest.TestCase):
    def test_loads_groups_and_front_matter_from_separate_page_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            group = root / "script-editor"
            group.mkdir()
            (group / "auto.md").write_text(
                "---\ntitle: Auto help\nsummary: Find descriptions\n---\n# Auto help\n\nUse Auto: to search.\n",
                encoding="utf-8",
            )

            groups = load_help_wiki(root)

            self.assertEqual([item.title for item in groups], ["Script Editor"])
            self.assertEqual(groups[0].pages[0].title, "Auto help")
            self.assertEqual(groups[0].pages[0].summary, "Find descriptions")
            self.assertIn("search", groups[0].pages[0].search_text)

    def test_missing_root_returns_an_empty_wiki(self) -> None:
        self.assertEqual(load_help_wiki(Path("does-not-exist")), ())


if __name__ == "__main__":
    unittest.main()
