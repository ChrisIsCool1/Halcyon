"""Backup helpers for file mutations performed by the manager."""

from __future__ import annotations

import logging
import shutil
from datetime import datetime
from pathlib import Path

from forge_content_manager.models import ForgePaths


class BackupService:
    """Create timestamped backups before files are overwritten or deleted."""

    def __init__(self, paths: ForgePaths) -> None:
        """Store the resolved Forge paths for later backup writes."""
        self._paths = paths
        self._logger = logging.getLogger(self.__class__.__name__)

    def backup_file(self, source_path: Path) -> Path | None:
        """Create a timestamped backup copy for an existing file."""
        if not source_path.exists() or not source_path.is_file():
            return None
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        suffix = "".join(source_path.suffixes) or ".bak"
        backup_name = f"{source_path.stem}_{timestamp}{suffix}"
        target_path = self._paths.backups_dir / backup_name
        counter = 2
        while target_path.exists():
            backup_name = f"{source_path.stem}_{timestamp}_{counter}{suffix}"
            target_path = self._paths.backups_dir / backup_name
            counter += 1
        shutil.copy2(source_path, target_path)
        self._logger.info("Created backup for %s at %s", source_path, target_path)
        return target_path
