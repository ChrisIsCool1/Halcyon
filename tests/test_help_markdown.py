"""Tests for inline Markdown rendered by the Help tab."""

from __future__ import annotations

import unittest

from forge_content_manager.ui.tabs.help_tab import _markdown_segments


class HelpMarkdownTests(unittest.TestCase):
    def test_recognizes_single_and_double_stars(self) -> None:
        self.assertEqual(
            _markdown_segments("Use **bold** and *italic* text."),
            [
                ("Use ", ()),
                ("bold", ("bold",)),
                (" and ", ()),
                ("italic", ("italic",)),
                (" text.", ()),
            ],
        )

    def test_recognizes_combined_emphasis(self) -> None:
        self.assertEqual(_markdown_segments("***important***"), [("important", ("bold", "italic"))])

    def test_preserves_unmatched_stars(self) -> None:
        self.assertEqual(_markdown_segments("A *literal star"), [("A *literal star", ())])


if __name__ == "__main__":
    unittest.main()
