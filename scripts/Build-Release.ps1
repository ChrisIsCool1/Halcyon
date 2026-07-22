[CmdletBinding()]
param(
    [string]$Version = "",
    [switch]$Clean
)

# This script builds a release ZIP for Halcyon using PyInstaller. 
# It reads the version from pyproject.toml and creates release/Halcyon-<version>-windows.zip. 
# Upload that ZIP to the matching GitHub Release. It contains Halcyon.exe, the README, and the license.
# Re-run with -Clean to replace a same-version local release artifact.

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not $Version) {
    # Fetches the version from pyproject.toml if not provided as a parameter
    $Version = (Select-String -Path "pyproject.toml" -Pattern '^version\s*=\s*"([^"]+)"').Matches[0].Groups[1].Value
}

# Defining paths for release and staging directories
$releaseRoot = Join-Path $projectRoot "release"
$stagingRoot = Join-Path $releaseRoot "Halcyon-$Version"
$archivePath = Join-Path $releaseRoot "Halcyon-$Version-windows.zip"
$workPath = Join-Path $projectRoot ".release-build"

if (Test-Path -LiteralPath $stagingRoot) {
    if (-not $Clean) {
        throw "Release staging folder already exists: $stagingRoot. Re-run with -Clean to replace it."
    }

    # If the staging folder exists and -Clean is specified, remove it to start fresh
    Remove-Item -LiteralPath $stagingRoot -Recurse -Force
}

if ((Test-Path -LiteralPath $archivePath) -and $Clean) {
    # If the release ZIP already exists and -Clean is specified, remove it to create a new one
    Remove-Item -LiteralPath $archivePath -Force
}

# Create a virtual environment if it doesn't exist
if (-not (Test-Path -LiteralPath ".\.venv")) {
    python -m venv .\.venv
}

# Activate the virtual environment and install PyInstaller
& .\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --workpath $workPath --distpath $stagingRoot ForgeContentManager.spec
if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed with exit code $LASTEXITCODE." }

# Copy the README and LICENSE files to the staging directory
Copy-Item -LiteralPath "README.md", "LICENSE.txt" -Destination $stagingRoot

# Compress the staging directory into a ZIP file
Compress-Archive -Path $stagingRoot -DestinationPath $archivePath -Force

# Log the creation of the release ZIP
Write-Host "Created $archivePath"
