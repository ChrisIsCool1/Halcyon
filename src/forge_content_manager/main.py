"""Application bootstrap and developer documentation command dispatch."""

import argparse
import sys
from datetime import date
from pathlib import Path

from forge_content_manager.constants import LOG_FILENAME, RARITY_LABELS
from forge_content_manager.logging_config import configure_logging
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.forge_paths import get_forge_paths
from forge_content_manager.services.image_service import ImageService
from forge_content_manager.services.package_service import PackageService
from forge_content_manager.services.settings_service import SettingsService
from forge_content_manager.models import CardImportInput


def _build_content_service() -> ForgeContentService:
    """Build the content service without starting the desktop UI."""
    paths = get_forge_paths()
    backup_service = BackupService(paths)
    edition_service = EditionService(paths, backup_service)
    image_service = ImageService(paths, backup_service)
    package_service = PackageService(paths, backup_service, edition_service)
    return ForgeContentService(
        paths=paths,
        backup_service=backup_service,
        edition_service=edition_service,
        image_service=image_service,
        package_service=package_service,
    )


def _create_set(name: str) -> None:
    service = _build_content_service()
    code = "".join(character for character in name.upper() if character.isalnum())[:5] or "CUSTOM"
    record = service.create_set(name=name, code=code, date_value=date.today().isoformat(), set_type="Custom")
    print(f"Created set '{record.name}' ({record.code}) at {record.file_path}")


def _create_card(set_name: str, card_name: str, rarity: str, script_path: Path, image_path: Path) -> None:
    from forge_content_manager.services.script_service import extract_card_name

    if not script_path.is_file():
        raise FileNotFoundError(f"Script file not found: {script_path}")
    if not image_path.is_file():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    service = _build_content_service()
    matching_sets = [item for item in service.list_sets() if item.name.casefold() == set_name.casefold()]
    if not matching_sets:
        raise ValueError(f"Set '{set_name}' was not found.")
    script_text = script_path.read_text(encoding="utf-8")
    script_card_name = extract_card_name(script_text)
    if script_card_name != card_name:
        raise ValueError(f"Script Name field is '{script_card_name or '<missing>'}', expected '{card_name}'.")
    summary = service.import_cards(matching_sets[0], [CardImportInput(script_text, image_path, rarity)])
    result = summary.results[0]
    if not result.success:
        raise ValueError(result.error or "Card import failed.")
    print(f"Created card '{card_name}' in set '{matching_sets[0].name}'.")


def _cli_main(arguments: list[str]) -> None:
    parser = argparse.ArgumentParser(prog="halcyon")
    subparsers = parser.add_subparsers(dest="command", required=True)
    set_parser = subparsers.add_parser("create_set", help="Create an empty custom set.")
    set_parser.add_argument("name")
    card_parser = subparsers.add_parser("create_card", help="Create a card from a script and image file.")
    card_parser.add_argument("set_name")
    card_parser.add_argument("card_name")
    card_parser.add_argument("rarity", choices=RARITY_LABELS)
    card_parser.add_argument("script_path", type=Path)
    card_parser.add_argument("image_path", type=Path)
    args = parser.parse_args(arguments)
    if args.command == "create_set":
        _create_set(args.name)
    else:
        _create_card(args.set_name, args.card_name, args.rarity, args.script_path, args.image_path)


def start() -> None:
    """Start the desktop application."""
    from forge_content_manager.ui.application import ForgeContentManagerApp

    paths = get_forge_paths()
    configure_logging(paths.logs_dir / LOG_FILENAME)
    backup_service = BackupService(paths)
    edition_service = EditionService(paths, backup_service)
    image_service = ImageService(paths, backup_service)
    package_service = PackageService(paths, backup_service, edition_service)
    content_service = ForgeContentService(
        paths=paths,
        backup_service=backup_service,
        edition_service=edition_service,
        image_service=image_service,
        package_service=package_service,
    )
    settings_service = SettingsService(paths)
    app = ForgeContentManagerApp(content_service=content_service, settings_service=settings_service)
    app.mainloop()


def main() -> None:
    """Dispatch the Halcyon command-line entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "docs":
        from forge_content_manager.devtools import main as documentation_main

        documentation_main(sys.argv[2:])
        return
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        start()
        return
    if len(sys.argv) > 1 and sys.argv[1] in {"create_set", "create_card", "--help", "-h"}:
        _cli_main(sys.argv[1:])
        return
    start()
