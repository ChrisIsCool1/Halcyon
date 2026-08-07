# Halcyon

A custom content editor for MTG Forge.

## Introduction

Named after the Thran capital, this is a small desktop application for managing custom cards on MTG Forge. I found the default way of going through folders manually a bit tedious, so this should automate the process a little. It can install custom cards, images, and sets that you can then use in whatever version of Forge you have. And it comes with a script editor that should be nicer to work with than editing scripts in a text document.

## Features

- **Begone, File Explorer:** Create, edit, rename, delete, import, and export custom Forge sets, all in app!
<img width="1358" height="929" alt="image" src="https://github.com/user-attachments/assets/4b7ea5a8-9968-4f0e-b15f-cafc137a84e1" />

- **Create a Set in Two Clicks:** One click to name and date it, and another to create it! Switch to the Import tab to quickly populate it with cards and images.
<img width="1356" height="927" alt="image" src="https://github.com/user-attachments/assets/ec1eca56-005a-435a-a6e6-f635f97b9468" />

- **Easy Card Editing:** Browse installed custom cards, edit scripts in place, replace images, and delete cards. No more going back and forth constantly between different folders.
<img width="1358" height="925" alt="image" src="https://github.com/user-attachments/assets/78507a70-412e-4a0e-b8d1-4caa97e15173" />

- **Import and Export Packages:** Import and export custom sets as `.forgepkg.zip` packages with collision handling. Share your wacky card sets with your friends!
<img width="1355" height="925" alt="image" src="https://github.com/user-attachments/assets/4e87085c-0ce2-47da-a002-00a5c7d136da" />

- **The Script Editor:** Think of this as VS Code for Forge! Draft Forge card scripts with syntax highlighting, keyword help, and autocompletion. If you import a cardsfolder from Forge, it even gives you a handy crossreference search of all existing cards right in the editor. The Script Editor also comes with some basic validation for things like SVar references.
<img width="1361" height="929" alt="image" src="https://github.com/user-attachments/assets/462768d3-68f0-4256-b683-5c8d6f078cfd" />


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

If you have a release ZIP, extract it and run the EXE. Otherwise, you can run it from source with:

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

## Maintaining Script Documentation

The Script Editor ships with a compact SQLite documentation pack and can import a replacement pack from Settings if a newer one is released. When new versions of Forge release new features or keywords, keeping up with the tabletop game, there are also dev commands you can run in Halcyon to update the documentation.

For command options, preset behavior, catalog format, and the full authoring workflow, see [the documentation CLI reference](docs/docs-cli.md).

## Notes

- Forge remains the authority for advanced script validation and gameplay logic correctness. This thing won't be what errors at you if your card scripts don't make sense.
- The manager only reads metadata fields such as `Name`, `Types`, `Oracle`, and `ManaCost` when required.
- Card images are converted to JPEG using Pillow and installed using Forge's `.fullborder.jpg` naming convention.

## Links / Shoutouts

- [MTG Forge](https://github.com/Card-Forge/forge)
- [MTG Forge Discord](https://discord.gg/HcPJNyD66a)
- [Manabrew](https://github.com/witchesofthehill/manabrew)
