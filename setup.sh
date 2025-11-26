#!/bin/bash
# Keykoe Setup Script for macOS/Linux

echo ""
echo "==================================="
echo "  Keykoe Installation Script"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[OK] Python is installed"
python3 --version
echo ""

# Check if venv exists
if [ -d "venv" ]; then
    echo "[OK] Virtual environment already exists"
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
    echo "[OK] Virtual environment created"
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo ""
echo "[INFO] Installing dependencies..."
echo "This may take a few minutes..."
echo ""
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

echo ""
echo "==================================="
echo "  Setup Complete!"
echo "==================================="
echo ""
echo "Next steps:"
echo "1. Make sure Ollama is installed from https://ollama.ai"
echo "2. Run: ollama pull llama3"
echo "3. Run: ollama serve (in a separate terminal)"
echo "4. Get Google Cloud credentials and save as keykoething.json"
echo "5. Run: python main.py"
echo ""
echo "For detailed instructions, see README.md or QUICKSTART.md"
echo ""
