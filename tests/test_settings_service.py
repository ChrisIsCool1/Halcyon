"""Tests for persisted application and Forge path settings."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from forge_content_manager.models import AppSettings, ForgePaths
from forge_content_manager.services.settings_service import SettingsService


class SettingsServiceTests(unittest.TestCase):
    def test_default_paths_are_preserved_without_overrides(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = ForgePaths(*(root / name for name in ("cards", "tokens", "editions", "decks", "images", "token-images", "backups", "logs", "settings.json")))
            service = SettingsService(paths)

            self.assertEqual(service.resolve_paths(AppSettings()), paths)

    def test_forge_path_overrides_round_trip_and_resolve(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            defaults = ForgePaths(*(root / name for name in ("cards", "tokens", "editions", "decks", "images", "token-images", "backups", "logs", "settings.json")))
            service = SettingsService(defaults)
            chosen_cards = root / "another-drive" / "cards"
            chosen_images = root / "another-drive" / "images"
            service.save(AppSettings(custom_cards_dir=chosen_cards, card_images_dir=chosen_images))

            loaded = service.load()
            resolved = service.resolve_paths(loaded)

            self.assertEqual(loaded.custom_cards_dir, chosen_cards)
            self.assertEqual(resolved.custom_cards_dir, chosen_cards)
            self.assertEqual(resolved.card_images_dir, chosen_images)
            self.assertEqual(resolved.custom_editions_dir, defaults.custom_editions_dir)
