"""Tests for Script Editor UI helpers that do not require a live window."""

from __future__ import annotations

import unittest

from forge_content_manager.ui.tabs.script_editor_tab import ScriptEditorTab


class ScriptEditorTabTests(unittest.TestCase):
    """Verify autocomplete identifies the term being replaced."""

    def test_completion_span_covers_an_identifier_at_any_caret_position(self) -> None:
        line = "A:AB$ ChangeZone | PrecostDesc$ Channel"
        start = line.index("ChangeZone")
        end = start + len("ChangeZone")

        for cursor in (start, start + 5, end):
            with self.subTest(cursor=cursor):
                self.assertEqual(ScriptEditorTab._completion_span_for(line, cursor), (start, end))

    def test_completion_span_rejects_non_identifier_positions(self) -> None:
        self.assertIsNone(ScriptEditorTab._completion_span_for("A:AB$ ChangeZone", 5))


if __name__ == "__main__":
    unittest.main()
