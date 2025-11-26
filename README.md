# Keykoe - An AI Companion

Keykoe is an AI companion chatbot designed to help NEETs and Hikikomoris come out of their shells and engage with the world. It features voice input/output capabilities and uses Ollama for local LLM inference with Google Cloud Text-to-Speech for natural audio output.

## Features

- 🎙️ Voice input via microphone
- 🔊 Natural speech output using Google Cloud TTS
- 🧠 Local LLM powered by Ollama (Llama3)
- 💬 Conversational AI with memory of recent exchanges
- 🎮 Built with Pygame for audio handling

## Prerequisites

Before running Keykoe, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running (Download from https://ollama.ai)
3. **Llama3 model** pulled in Ollama (`ollama pull llama3`)
4. **Google Cloud credentials** for Text-to-Speech (see setup instructions below)
5. **ffmpeg** installed on your system (for audio processing)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/SG-Andres/ENED1001C-project-Keykoe.git
cd ENED1001C-project-Keykoe
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Google Cloud Credentials

1. Create a Google Cloud project at https://console.cloud.google.com
2. Enable the Text-to-Speech API
3. Create a service account and download the JSON key file
4. Rename the JSON file to `keykoething.json` and place it in the project root directory

Your project structure should look like:
```
ENED1001C-project-Keykoe/
├── main.py
├── keykoething.json          # Your Google Cloud credentials
├── requirements.txt
├── README.md
└── index-tts/
```

### Step 5: Start Ollama

Before running Keykoe, make sure Ollama is running:

```bash
ollama serve
```

In a new terminal, ensure Llama3 is available:

```bash
ollama pull llama3
```

### Step 6: Run Keykoe

```bash
python main.py
```

## Usage

Once started, Keykoe will greet you. Simply speak into your microphone to interact with the companion. Commands:

- Speak naturally to have a conversation
- Say "exit", "goodbye", or "quit" to end the conversation
- Keykoe will respond with both text and voice

## Troubleshooting

### Audio Input Not Working
- Ensure your microphone is connected and recognized by your system
- Check audio input levels in your system settings
- Try running with a simple test script to verify microphone access

### Google Cloud TTS Not Working
- Verify `keykoething.json` exists in the project root
- Check that the Text-to-Speech API is enabled in your Google Cloud project
- Ensure your service account has the "Cloud Text-to-Speech User" role

### Ollama Connection Issues
- Ensure Ollama is running (`ollama serve`)
- Check that Llama3 model is pulled (`ollama pull llama3`)
- Verify Ollama is accessible at `http://localhost:11434` (default)

### Missing Dependencies
If you encounter import errors, reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

## Project Structure

- `main.py` - Main chatbot application
- `requirements.txt` - Python dependencies
- `keykoething.json` - Google Cloud credentials (not included in repo)
- `index-tts/` - Text-to-Speech integration submodule

## Requirements

All dependencies are listed in `requirements.txt`. Key packages:
- **pygame** - Audio playback
- **google-cloud-texttospeech** - Natural speech synthesis
- **langchain** - LLM framework
- **langchain-ollama** - Ollama integration
- **RealtimeSTT** - Voice recording

## Development

Created by Andres Sanchez-Gonzalez (10/26/2025)

Last updated: 11/26/2025

## License

[Add your license here]

## Support

For issues and questions, please open an issue on the GitHub repository. 
