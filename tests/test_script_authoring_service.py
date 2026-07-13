"""Tests for lightweight Forge script authoring reference data."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from forge_content_manager.services.script_authoring_service import ScriptAuthoringService


class ScriptAuthoringServiceTests(unittest.TestCase):
    """Exercise guide lookup and optional reference-card behavior."""

    def test_metadata_and_factory_terms_are_available(self) -> None:
        service = ScriptAuthoringService(reference_cards_dir=Path("missing-reference-folder"))
        self.assertEqual(service.lookup("Name").category, "Card property")
        self.assertIsNotNone(service.lookup("Pump"))
        self.assertEqual(service.lookup("K:Vigilance").description, "Vigilance allows a creature to attack without tapping.")
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


if __name__ == "__main__":
    unittest.main()
