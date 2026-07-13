"""Tests for mined documentation sources and compiled documentation packs."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from forge_content_manager.devtools import extract_terms, sync_catalog, write_discoveries
from forge_content_manager.services.documentation_pack import DocumentationRecord, compile_pack, load_pack, validate_pack
from forge_content_manager.services.script_authoring_service import ScriptAuthoringService


class DocumentationPackTests(unittest.TestCase):
    def test_extract_deduplicates_and_sorts_custom_pattern(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.txt").write_text("K:Vigilance\nK:Trample\n", encoding="utf-8")
            (root / "two.txt").write_text("K:Vigilance\n", encoding="utf-8")
            self.assertEqual(extract_terms(root, r"(?m)^K:(.+)$"), ["Trample", "Vigilance"])

    def test_extract_reports_progress_against_precounted_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.txt").write_text("K:Vigilance\n", encoding="utf-8")
            (root / "two.txt").write_text("K:Trample\n", encoding="utf-8")
            updates: list[tuple[int, int]] = []
            extract_terms(root, r"(?m)^K:(.+)$", lambda completed, total: updates.append((completed, total)))
            self.assertEqual(updates[0], (0, 2))
            self.assertEqual(updates[-1], (2, 2))

    def test_sync_preserves_existing_authored_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            discoveries, catalog = root / "found.md", root / "keywords.md"
            write_discoveries(discoveries, ["K:Trample", "K:Vigilance"], "Found")
            catalog.write_text("# Keywords\n\n## `K:Vigilance`\n\nAuthored explanation.\n", encoding="utf-8")
            self.assertEqual(sync_catalog(discoveries, catalog), 1)
            content = catalog.read_text(encoding="utf-8")
            self.assertIn("Authored explanation.", content)
            self.assertIn("## `K:Trample`", content)

    def test_compiled_pack_validates_and_resolves_context(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pack = Path(directory) / "documentation.sqlite3"
            compile_pack(pack, [
                DocumentationRecord("K:Vigilance", "Keywords", "Attacks without tapping."),
                DocumentationRecord("Mode$ Attacks", "Trigger modes", "Triggers when this attacks."),
                DocumentationRecord("ValidTgts$", "Parameters", "Defines legal targets."),
            ], "test-1")
            self.assertEqual(validate_pack(pack), "test-1")
            self.assertEqual(len(load_pack(pack)), 3)
            service = ScriptAuthoringService(Path("missing"), Path(directory) / "cards.sqlite3", pack)
            self.assertEqual(service.lookup_context("K:Vigilance", 6).description, "Attacks without tapping.")
            self.assertEqual(service.lookup_context("T:Mode$ Attacks | Execute$ X", 12).description, "Triggers when this attacks.")
            self.assertEqual(service.lookup_context("A:SP$ Pump | ValidTgts$ Creature", 23).description, "Defines legal targets.")

    def test_invalid_pack_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "not-a-pack.sqlite3"
            invalid.write_text("not sqlite", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_pack(invalid)


if __name__ == "__main__":
    unittest.main()
