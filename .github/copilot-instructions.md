# GitHub Copilot Instructions

## Project overview

Halcyon is a Windows 10/11 desktop application for managing custom Magic: The Gathering card content used by MTG Forge. It is a Python 3.12 project using `customtkinter` for the UI and Pillow for card-image conversion.

## Repository layout

- `src/forge_content_manager/main.py` is the application composition root and console entry point.
- `src/forge_content_manager/models.py` contains shared dataclasses, enums, and value objects.
- `src/forge_content_manager/services/` contains filesystem, parsing, backup, package, image, and content workflows.
- `src/forge_content_manager/ui/` contains CustomTkinter views, dialogs, reusable widgets, and tabs.
- `scripting_docs/` is reference material for the Forge card-scripting API. Consult it when work concerns card-script semantics.

Keep UI code focused on display, event handling, and user feedback. Put file operations and reusable business workflows in services. `ForgeContentService` is the UI-facing façade for coordinated content operations; preserve that boundary when practical.

## Python conventions

- Target Python 3.12 and use built-in generic types such as `list[str]`, `dict[str, str]`, and `Path | None`.
- Include `from __future__ import annotations` in modules that use forward references or modern annotations, matching the existing project style.
- Use `pathlib.Path` rather than string-based path manipulation.
- Write code that tells a story and is easy to read. Add comments for non-obvious logic, but avoid redundant comments that restate the code.
- Add docstrings to all public classes and methods that explain their purpose and usage. Describe parameters, return values, and any exceptions raised on functions you write. Use clear, typed signatures and small helpers for repeated logic.
- Use `logging` for operational details; do not add `print()` calls to application code.
- Surface expected user-facing failures as clear `ValueError` messages where that matches existing service behavior; UI code should present those errors to the user.
- Avoid adding dependencies unless they materially benefit the application. If one is needed, update `pyproject.toml`.

## Forge content safety rules

- Preserve Forge card-script text exactly unless the user explicitly requests a script edit. Do not parse, normalize, reformat, or attempt to validate gameplay logic beyond the project’s basic metadata checks.
- Treat Forge as the authority for advanced card-script validation and gameplay correctness.
- Card scripts are stored as UTF-8 `.txt` files using the canonical normalized filename from `script_service.resolve_script_path()`.
- Card images use Forge's `<card name>.fullborder.jpg` convention. Use the existing image service for conversion, installation, lookup, and rename operations.
- Resolve Forge directories through `get_forge_paths()`; do not hard-code user-specific paths. The application relies on `%APPDATA%` and `%LOCALAPPDATA%` on Windows.
- Before changing or deleting a Forge edition, card script, or image, preserve the existing backup behavior through `BackupService`.
- Keep edition-file changes and card/image changes consistent. For example, a renamed or deleted card must have its edition references updated through `EditionService`.
- Be careful with filesystem mutations: create required parent directories, handle missing optional files safely, and avoid deleting assets shared by multiple sets.

## UI conventions

- Use `customtkinter` (`ctk`) and follow the existing tab-based layout in `ui/application.py`.
- Keep the UI responsive during multi-file work. Use the established progress-callback pattern for batch operations and update UI controls safely.
- Refresh dependent views after successful content changes using the application’s refresh callbacks.
- Preserve support for system, light, and dark appearance modes.

## Validation and verification

- Run the project with `python -m forge_content_manager` after installing it in editable mode.
- Build the Halcyon distributable with `pyinstaller ForgeContentManager.spec` when packaging-related files change.
- When changing Forge script handling, test filenames with punctuation, Unicode/display names, missing metadata, absent images, and cards that belong to multiple sets.
- Do not commit generated output such as `.venv/`, `build/`, `dist/`, cache files, or copied card scripts under `scripting_docs/cards/`.
