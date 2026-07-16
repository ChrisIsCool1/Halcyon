"""Application bootstrap and developer documentation command dispatch."""

import sys

from forge_content_manager.constants import LOG_FILENAME
from forge_content_manager.logging_config import configure_logging
from forge_content_manager.services.backup_service import BackupService
from forge_content_manager.services.content_service import ForgeContentService
from forge_content_manager.services.edition_service import EditionService
from forge_content_manager.services.forge_paths import get_forge_paths
from forge_content_manager.services.image_service import ImageService
from forge_content_manager.services.package_service import PackageService
from forge_content_manager.services.settings_service import SettingsService
from forge_content_manager.ui.application import ForgeContentManagerApp


def start() -> None:
    """Start the desktop application."""
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
    start()
