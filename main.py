# keykoe: An AI Companion by Andres Sanchez-Gonzalez 10.26.2025
import os
import uuid
import pygame
from google.cloud import texttospeech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keykoething.json"
client = texttospeech.TextToSpeechClient()
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from RealtimeSTT import AudioToTextRecorder
pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until audio finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speak_google_tts(text):
    # Build request
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-F"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Generate filename
    filename = f"tts_{uuid.uuid4().hex}.mp3"

    # Send TTS request
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Save file
    with open(filename, "wb") as out:
        out.write(response.audio_content)

    # Play audio
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # WAIT until playback finishes
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

        # Unload file from mixer
        pygame.mixer.music.unload()

    except Exception as e:
        print("Audio playback error:", e)

    # Now safe to delete
    try:
        os.remove(filename)
    except Exception as e:
        print("File delete error:", e)




#SET UP/CONTEXT
template = """ 
You are Keykoe, a helpful and friendly AI companion with a warm and engaging personality similar to that of an anime girl and Paimon from Genshin Impact whose main goal is to help NEETs or Hikikomoris come out of their shells and engage with the world around them. 
You are empathetic, patient, and always ready to listen. You provide encouragement, advice, and companionship to help users feel more connected and motivated.
Encourage users to take small steps towards social interaction and personal growth, while always being respectful of their boundaries and comfort levels.
Try not to be too formal or robotic in your responses, instead aim for a conversational and relatable tone while not being too verbose or drag on too much.

Conversation so far:
{Context}

Human: {Question}
Keykoe:
"""

# FIND WAY TO "FIX" MEMORY LATER 11/3/25 Fixed 11/3/25
#11/3/25 sucessfully implemented simple memory by appending context and trimming to last 10 exchanges
#and also added voice to text input via microphone
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

#main loop
def handle_conversation():
    context = ""
    print("Hi! My name is Keykoe, your AI companion. How can I help you today?")
    
    while True:
        # Input via microphone
        with AudioToTextRecorder() as recorder:
            user_input = recorder.text().strip()
        print(f"You (from mic): {user_input}")

        # EXIT condition
        if user_input.lower() in ["exit", "goodbye", "quit"]:
            goodbye_prompt = "Say a cute goodbye message and end the conversation warmly."
            result = chain.invoke({"Context": context, "Question": goodbye_prompt})
            keykoe_text = result.strip()

            print(f"Keykoe: {keykoe_text}")
            speak_google_tts(keykoe_text)
            break

        # Keykoe’s response
        result = chain.invoke({"Context": context, "Question": user_input})
        keykoe_text = result.strip()

        print(f"Keykoe: {keykoe_text}")
        speak_google_tts(keykoe_text)
        # Update memory (keep last 10 exchanges)
        context += f"\nHuman: {user_input}\nKeykoe: {result}"
        context = "\n".join(context.splitlines()[-20:])

if __name__ == "__main__":
    handle_conversation()
