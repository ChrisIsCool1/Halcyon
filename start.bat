@echo off
cd /d "%~dp0"
set "PYTHONPATH=%CD%\src;%PYTHONPATH%"
.venv\Scripts\python.exe -m forge_content_manager
