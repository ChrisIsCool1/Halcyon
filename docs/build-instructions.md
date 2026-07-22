# Build With PyInstaller

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Create a release ZIP (run from PowerShell at the repository root):

```powershell
.\scripts\Build-Release.ps1
```

If Windows blocks the script, you can run it like this:

```powershell
pwsh -ExecutionPolicy Bypass -File .\scripts\Build-Release.ps1 -Clean
```

There's no virus in that script; it's fully commented and open source, so you can verify what it does before running. The `-Clean` option removes any existing release artifacts before creating a new one.

The script reads the version from `pyproject.toml` and creates `release/Halcyon-<version>-windows.zip`. Upload that ZIP to the matching GitHub Release. It contains `Halcyon.exe`, the README, and the license; users should extract the ZIP before launching the EXE. Re-run with `-Clean` to replace a same-version local release artifact.

The Script Editor bundles the Forge scripting Markdown guides for easy reference. To search full reference card scripts in a packaged build, import a local unzipped Forge `cardsfolder` directory in Settings, and it will generate a lookup SQLite database that it can search through.
