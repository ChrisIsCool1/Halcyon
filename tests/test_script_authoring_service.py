"""Tests for lightweight Forge script authoring reference data."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from forge_content_manager.services.documentation_pack import DocumentationRecord, compile_pack
from forge_content_manager.services.script_authoring_service import ScriptAuthoringService


class ScriptAuthoringServiceTests(unittest.TestCase):
    """Exercise guide lookup and optional reference-card behavior."""

    def test_metadata_and_factory_terms_are_available(self) -> None:
        service = ScriptAuthoringService(reference_cards_dir=Path("missing-reference-folder"))
        self.assertEqual(service.lookup("Name").category, "Card property")
        self.assertIsNotNone(service.lookup("Pump"))
        self.assertIsNotNone(service.lookup("Vigilance"))
        self.assertIn("ManaCost", [item.name for item in service.complete("Mana")])

    def test_optional_reference_folder_is_searchable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            script = folder / "sample.txt"
            script.write_text("Name:Sample Adept\nTypes:Creature Wizard\n", encoding="utf-8")
            service = ScriptAuthoringService(reference_cards_dir=folder, database_path=folder / "cards.sqlite3")
            self.assertTrue(service.wait_until_ready())
            cards = service.search_reference_cards("adept")
            self.assertEqual([card.name for card in cards], ["Sample Adept"])
            self.assertEqual(service.load_reference_card(cards[0]), script.read_text(encoding="utf-8"))

    def test_missing_reference_folder_is_safe(self) -> None:
        service = ScriptAuthoringService(reference_cards_dir=Path("does-not-exist"), database_path=Path("does-not-exist.sqlite3"))
        self.assertEqual(service.search_reference_cards("anything"), [])
        self.assertIn("unavailable", service.reference_status())

    def test_contextual_parameters_prefer_family_records_and_fall_back_to_global_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            pack = Path(temporary_directory) / "documentation.sqlite3"
            contexts = {
                "A": ("Pump", "A:SP$ Pump"),
                "T": ("Attacks", "T:Mode$ Attacks"),
                "S": ("Continuous", "S:Mode$ Continuous"),
                "R": ("Moved", "R:Event$ Moved"),
            }
            records = [
                DocumentationRecord("Shared$", "Global parameter", "Global documentation.", ("global-value",)),
                DocumentationRecord("GlobalOnly$", "Global parameter", "Fallback documentation.", ("fallback-value",)),
            ]
            for scope, (family, _) in contexts.items():
                records.append(DocumentationRecord("Shared$", f"{scope} parameter", f"{scope} documentation.", (f"{scope}-value",), scope=f"{scope}:{family}"))
            compile_pack(pack, records)
            service = ScriptAuthoringService(Path("missing"), Path(temporary_directory) / "cards.sqlite3", pack)

            for scope, (family, line_start) in contexts.items():
                with self.subTest(scope=scope):
                    completions = service.complete("", scope=f"{scope}:{family}")
                    self.assertEqual([item.name for item in completions], ["GlobalOnly$", "Shared$"])
                    self.assertEqual(next(item for item in completions if item.name == "Shared$").description, f"{scope} documentation.")

                    self.assertEqual(
                        [item.name for item in service.complete_context(f"{line_start} | Sh", len(f"{line_start} | Sh"), "Sh")],
                        ["Shared$"],
                    )
                    self.assertEqual(
                        [item.name for item in service.complete_context(f"{line_start} | Gl", len(f"{line_start} | Gl"), "Gl")],
                        ["GlobalOnly$"],
                    )

                    local_line = f"{line_start} | Shared$ "
                    self.assertEqual([item.name for item in service.complete_context(local_line, len(local_line), "")], [f"{scope}-value"])
                    self.assertEqual(service.lookup_context(local_line, local_line.index("Shared") + 2).description, f"{scope} documentation.")

                    fallback_line = f"{line_start} | GlobalOnly$ "
                    self.assertEqual([item.name for item in service.complete_context(fallback_line, len(fallback_line), "")], ["fallback-value"])
                    self.assertEqual(service.lookup_context(fallback_line, fallback_line.index("GlobalOnly") + 2).description, "Fallback documentation.")


if __name__ == "__main__":
    unittest.main()
