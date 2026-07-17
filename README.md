# Halcyon

A custom content editor for MTG Forge.

## Introduction

Named after the Thran capital, this is a small desktop application for managing custom cards on MTG Forge. I found the default way of going through folders manually a bit tedious, so this should automate the process a little. It can install custom cards, images, and sets that you can then use in whatever version of Forge you have. And it comes with a script editor that should be nicer to work with than editing scripts in a text document.

## Features

- **Begone, File Explorer:** Create, edit, rename, delete, import, and export custom Forge sets, all in app!
- **Create a Set in One Click:** Jot down a bunch of scripts, import a few images, click Import and you're done!
- **Easy Set Editing:** Browse installed custom cards, edit scripts in place, replace images, and delete cards. No more going back and forth constantly between different folders.
- **Import and Export Packages:** Import and export `.forgepkg.zip` packages with collision handling.
- **The Script Editor:** Think of this as VS Code for Forge! Draft Forge card scripts with syntax highlighting, keyword help, and autocompletion. If you import a cardsfolder from Forge, it even gives you a handy crossreference search of all existing cards right in the editor. The Script Editor also comes with some basic validation for things like SVar references.

## Requirements

- Python 3.12
- Windows 10 or 11
- MTG Forge custom content folders available under `%APPDATA%` and `%LOCALAPPDATA%`
- MTG Forge version newer than or equal to 2.0.12 (Secrets of Strixhaven Release)

## Install

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run

```powershell
halcyon start
```

If you're a command line fan, you can also create sets and cards directly from the CLI:

```powershell
halcyon create_set "My Custom Set"
halcyon create_card "My Custom Set" "Example Card" Common .\example-card.txt .\example-card.png
```

`create_card` expects the script's `Name:` field to match the card name argument; it will error without creating anything if they're different. The image is converted to Forge's JPEG format when installed.

The application creates any missing Forge custom content directories automatically, so don't worry about creating them if they aren't present.

## Build With PyInstaller

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build the executable:

```powershell
pyinstaller ForgeContentManager.spec
```

The bundled executable will be created under `dist/Halcyon/`.

The Script Editor bundles the Forge scripting Markdown guides for easy reference. To search full reference
card scripts in a packaged build, import a local unzipped Forge `cardsfolder` directory in Settings, and it will generate a lookup SQLite database that it can search through.

## Maintaining Script Documentation

The Script Editor ships with a compact SQLite documentation pack and can import a replacement
pack from Settings if a newer one is released. When new versions of Forge release new features or keywords, keeping up with the
tabletop game, there are also dev commands you can run in Halcyon to update the documentation.

For command options, preset behavior, catalog format, and the full authoring workflow,
see [the documentation CLI reference](docs/docs-cli.md).

Run this command to extract keywords from the given unzipped cardsfolder and update the database all in one step:

```powershell
halcyon docs refresh --cards-dir scripting_docs/cards/cardsfolder
```

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

- Forge remains the authority for advanced script validation and gameplay logic correctness. This thing won't be what errors at you if your card scripts don't make sense.
- The manager only reads metadata fields such as `Name`, `Types`, `Oracle`, and `ManaCost` when required.
- Card images are converted to JPEG using Pillow and installed using Forge's `.fullborder.jpg` naming convention.

## Links / Shoutouts

- [MTG Forge](https://github.com/Card-Forge/forge)
- [MTG Forge Discord](https://discord.gg/HcPJNyD66a)
- [Manabrew](https://github.com/witchesofthehill/manabrew)
