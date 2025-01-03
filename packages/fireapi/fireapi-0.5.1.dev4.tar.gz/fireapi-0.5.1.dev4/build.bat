@echo off
setlocal enabledelayedexpansion

:: Clean previous builds
if exist "dist" rd /s /q "dist"
if exist "build" rd /s /q "build"
if exist "*.egg-info" rd /s /q "*.egg-info"

:: Format code with Ruff
echo Formatting code...
ruff format .
if errorlevel 1 (
    echo Code formatting failed.
    exit /b 1
)

:: Run Ruff checks
echo Running Ruff checks...
ruff check . --fix
if errorlevel 1 (
    echo Ruff checks failed.
    exit /b 1
)

:: Run type checking
echo Running type checks...
mypy src/fireapi
if errorlevel 1 (
    echo Type checking failed.
    exit /b 1
)

:: Build the library
echo Building package...
python -m build
if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

:: Ask for confirmation before uploading
set /p upload="Do you want to upload to PyPI? (y/n): "
if /i "%upload%"=="y" (
    echo Uploading to PyPI...
    twine upload dist/*
)

echo Build process completed.
endlocal
