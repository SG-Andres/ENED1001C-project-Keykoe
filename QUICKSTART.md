# Keykoe - Quick Start Guide

Get Keykoe running in 5 minutes!

## ⚡ Quick Setup

### 1. Install Prerequisites
- Download and install **Python 3.8+** from https://www.python.org
- Download and install **Ollama** from https://ollama.ai
- Download and install **ffmpeg** (Windows: use https://www.gyan.dev/ffmpeg/builds/)

### 2. Clone & Setup
```bash
git clone https://github.com/SG-Andres/ENED1001C-project-Keykoe.git
cd ENED1001C-project-Keykoe
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 3. Get Ollama Ready
```bash
ollama pull llama3
ollama serve
```
(Keep this running in a separate terminal)

### 4. Set Up Google Cloud
1. Go to https://console.cloud.google.com
2. Create a new project
3. Enable "Cloud Text-to-Speech API"
4. Create a Service Account (IAM → Service Accounts)
5. Create a key (JSON format)
6. Download the JSON file and rename it to `keykoething.json`
7. Place it in the project root directory

### 5. Run Keykoe
```bash
python main.py
```

That's it! Start talking to Keykoe! 🎉

---

## 📋 Detailed Requirements

| Requirement | Purpose | Version |
|---|---|---|
| Python | Runtime | 3.8+ |
| Ollama + Llama3 | Local LLM | Latest |
| Google Cloud Account | TTS API | Free tier available |
| ffmpeg | Audio processing | Latest |
| Microphone | Voice input | Any |

## 🔧 System Requirements

- **CPU**: 4+ cores recommended
- **RAM**: 8GB minimum (16GB recommended for smooth LLM inference)
- **Storage**: 5GB for Ollama + Llama3 model
- **Internet**: Required for Google Cloud TTS

## ✅ Verification

Before running, verify everything is set up:

```bash
# Check Python
python --version

# Check Ollama is running (should return model info)
curl http://localhost:11434/api/tags

# Check Google Cloud credentials
python -c "import json; json.load(open('keykoething.json'))"
```

## 🆘 Common Issues

**"ModuleNotFoundError: No module named 'X'"**
→ Run `pip install -r requirements.txt`

**"Cannot connect to Ollama"**
→ Make sure `ollama serve` is running in another terminal

**"Google Cloud credentials error"**
→ Verify `keykoething.json` exists in the project root

**Microphone not detected**
→ Check system audio settings and try a different USB microphone

---

For more help, see README.md or open an issue on GitHub!
