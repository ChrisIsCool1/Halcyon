"""Import helpers for optional Forge reference cards."""

from __future__ import annotations

import hashlib
import os
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


def extract_reference_cards_zip(archive_path: Path, storage_directory: Path) -> Path:
    """Safely extract a cardsfolder ZIP into a persistent, app-managed directory.

    The source archive is only read. Extracted files are keyed by the archive's
    content hash so a later import cannot overwrite files currently being indexed.

    Raises:
        ValueError: If the archive is invalid, unsafe, or contains no card scripts.
        OSError: If the archive cannot be read or extracted.
    """
    archive_path = archive_path.expanduser().resolve()
    if not archive_path.is_file():
        raise ValueError("Choose an existing cardsfolder ZIP archive.")

    digest = _sha256_file(archive_path)
    storage_directory.mkdir(parents=True, exist_ok=True)
    destination = storage_directory / digest
    completion_marker = destination / ".halcyon-extraction-complete"
    if completion_marker.is_file() and _contains_card_scripts(destination):
        return destination

    try:
        with zipfile.ZipFile(archive_path) as archive:
            entries = archive.infolist()
            if not entries:
                raise ValueError("The selected ZIP archive is empty.")
            safe_entries = [(_safe_member_path(entry), entry) for entry in entries]
            if not any(not entry.is_dir() and relative.suffix.casefold() == ".txt" for relative, entry in safe_entries):
                raise ValueError("The selected ZIP archive does not contain any card-script .txt files.")

            staging_directory = Path(tempfile.mkdtemp(prefix=f".{digest}.", dir=storage_directory))
            try:
                for relative, entry in safe_entries:
                    target = staging_directory.joinpath(*relative.parts)
                    if not target.resolve().is_relative_to(staging_directory.resolve()):
                        raise ValueError("The ZIP archive contains an unsafe file path.")
                    if entry.is_dir():
                        target.mkdir(parents=True, exist_ok=True)
                        continue
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(entry) as source, target.open("wb") as output:
                        shutil.copyfileobj(source, output)
                if not _contains_card_scripts(staging_directory):
                    raise ValueError("The selected ZIP archive does not contain any card-script .txt files.")
                (staging_directory / ".halcyon-extraction-complete").write_text(digest, encoding="ascii")
                if destination.exists():
                    shutil.rmtree(destination)
                os.replace(staging_directory, destination)
            except Exception:
                shutil.rmtree(staging_directory, ignore_errors=True)
                raise
    except zipfile.BadZipFile as exc:
        raise ValueError("The selected file is not a valid ZIP archive.") from exc
    except RuntimeError as exc:
        raise ValueError("The selected ZIP archive is encrypted or uses an unsupported compression method.") from exc
    return destination


def _safe_member_path(entry: zipfile.ZipInfo) -> Path:
    """Convert a ZIP entry to a safe relative Windows-compatible path."""
    name = entry.filename
    if "\\" in name:
        raise ValueError("The ZIP archive contains an unsafe file path.")
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError("The ZIP archive contains an unsafe file path.")
    if any(":" in part or part.rstrip(" .") in {"", ".", ".."} for part in path.parts):
        raise ValueError("The ZIP archive contains an unsafe file path.")
    unix_mode = entry.external_attr >> 16
    if stat.S_ISLNK(unix_mode):
        raise ValueError("The ZIP archive contains a symbolic link, which cannot be imported.")
    return Path(*path.parts)


def _sha256_file(path: Path) -> str:
    """Return a streaming SHA-256 digest for an archive."""
    digest = hashlib.sha256()
    with path.open("rb") as archive:
        for chunk in iter(lambda: archive.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _contains_card_scripts(directory: Path) -> bool:
    """Return whether a directory contains at least one recursive .txt script."""
    return any(path.is_file() and path.suffix.casefold() == ".txt" for path in directory.rglob("*.txt"))
