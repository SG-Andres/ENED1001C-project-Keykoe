@echo off
REM Keykoe Setup Script for Windows

echo.
echo ===================================
echo  Keykoe Installation Script
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please download Python from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check if venv exists
if exist venv (
    echo [OK] Virtual environment already exists
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

echo.
echo [INFO] Installing dependencies...
echo This may take a few minutes...
echo.
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ===================================
echo  Setup Complete!
echo ===================================
echo.
echo Next steps:
echo 1. Make sure Ollama is installed from https://ollama.ai
echo 2. Run: ollama pull llama3
echo 3. Run: ollama serve (in a separate terminal)
echo 4. Get Google Cloud credentials and save as keykoething.json
echo 5. Run: python main.py
echo.
echo For detailed instructions, see README.md or QUICKSTART.md
echo.
pause
