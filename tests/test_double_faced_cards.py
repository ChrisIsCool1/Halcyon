"""Regression coverage for Forge alternate-face cards."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image

from forge_content_manager.devtools import extract_preset
from forge_content_manager.models import CardImportInput, ForgePaths
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.forge_paths import ensure_directories
from forge_content_manager.services.image_service import ImageService
from forge_content_manager.services.package_service import PackageService
from forge_content_manager.services.script_service import extract_card_face_names, validate_script


SCRIPT = """Name:Barkchannel Pathway
ManaCost:no cost
Types:Land
AlternateMode:Modal
Oracle:{T}: Add {G}.

ALTERNATE

Name:Tidechannel Pathway
ManaCost:no cost
Types:Land
Oracle:{T}: Add {U}.
"""


class DoubleFacedCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.paths = ForgePaths(*(root / name for name in ("cards", "tokens", "editions", "decks", "images", "token-images", "backups", "logs", "settings.json")))
        ensure_directories(self.paths)
        backup = BackupService(self.paths)
        edition = EditionService(self.paths, backup)
        image = ImageService(self.paths, backup)
        self.service = ForgeContentService(self.paths, backup, edition, image, PackageService(self.paths, backup, edition))
        self.set_record = self.service.create_set("Kaldheim", "KHM", "2021-02-05", "Custom")
        self.front_image = root / "front.png"
        self.back_image = root / "back.png"
        Image.new("RGB", (10, 10), "green").save(self.front_image)
        Image.new("RGB", (10, 10), "blue").save(self.back_image)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_import_saves_both_faces_but_only_front_in_edition(self) -> None:
        result = self.service.import_cards(self.set_record, [CardImportInput(SCRIPT, self.front_image, "Rare", self.back_image)])

        self.assertEqual((result.imported_count, result.failed_count), (1, 0))
        document = self.service.edition_service.parse_edition_file(self.set_record.file_path)
        self.assertEqual([card.card_name for card in document.cards], ["Barkchannel Pathway"])
        record = self.service.scan_cards()[0]
        self.assertEqual(record.face_names, ["Barkchannel Pathway", "Tidechannel Pathway"])
        self.assertTrue(record.image_present)
        self.assertTrue(all(path is not None and path.exists() for path in record.image_paths))

    def test_second_image_requires_alternate_metadata(self) -> None:
        single_face = "Name:Forest\nManaCost:no cost\nTypes:Land\nOracle:{T}: Add {G}.\n"
        messages = validate_script(single_face, "Kaldheim", self.front_image, self.back_image)

        self.assertIn("A second image requires an Alternate or AlternateMode field.", [message.message for message in messages])

    def test_saving_a_renamed_alternate_face_renames_its_image(self) -> None:
        self.service.import_cards(self.set_record, [CardImportInput(SCRIPT, self.front_image, "Rare", self.back_image)])
        record = self.service.scan_cards()[0]
        updated = self.service.save_script(record, SCRIPT.replace("Tidechannel Pathway", "Riverchannel Pathway"))

        self.assertEqual(updated.face_names[1], "Riverchannel Pathway")
        self.assertIsNotNone(updated.image_paths[1])
        self.assertTrue(updated.image_paths[1].exists())
        self.assertIsNone(self.service.image_service.find_image("KHM", "Tidechannel Pathway"))

    def test_face_name_parser_preserves_front_to_back_order(self) -> None:
        self.assertEqual(extract_card_face_names(SCRIPT), ["Barkchannel Pathway", "Tidechannel Pathway"])

    def test_alternate_mode_documentation_preset_discovers_modes(self) -> None:
        cards_dir = Path(self.temp.name) / "reference-cards"
        cards_dir.mkdir()
        (cards_dir / "pathway.txt").write_text(SCRIPT, encoding="utf-8")
        output = Path(self.temp.name) / "alternate-modes.md"

        self.assertEqual(extract_preset(cards_dir, "alternate-mode", output), 1)
        self.assertIn("Modal", output.read_text(encoding="utf-8"))
