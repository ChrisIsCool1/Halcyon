# Forge Custom Content Manager

Desktop application for managing custom Magic: The Gathering cards and sets for MTG Forge on Windows 10 and 11.

## Features

- Create, edit, rename, delete, import, and export custom Forge sets.
- Batch import multiple card scripts with optional image conversion and installation.
- Browse installed custom cards, edit scripts in place, replace images, and delete cards.
- Preserve Forge script contents exactly and validate only basic metadata requirements.
- Create timestamped backups before edition, script, or image changes.
- Import and export `.forgepkg.zip` packages with collision handling.
- Switch between system, light, and dark appearance modes.

## Requirements

- Python 3.12
- Windows 10 or 11
- MTG Forge custom content folders available under `%APPDATA%` and `%LOCALAPPDATA%`

## Install

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run

```powershell
python -m forge_content_manager
```

The application creates any missing Forge custom content directories automatically.

## Build With PyInstaller

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build the executable:

```powershell
pyinstaller ForgeContentManager.spec
```

The bundled executable will be created under `dist/ForgeContentManager/`.

## Project Structure

```text
src/forge_content_manager/
	constants.py
	logging_config.py
	main.py
	models.py
	services/
	ui/
```

## Notes

- Forge remains the authority for advanced script validation and gameplay logic correctness.
- The manager only reads metadata fields such as `Name`, `Types`, `Oracle`, and `ManaCost` when required.
- Card images are converted to JPEG using Pillow and installed using Forge's `.fullborder.jpg` naming convention.
