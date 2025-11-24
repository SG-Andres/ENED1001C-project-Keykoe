# keykoe: An AI Companion by Andres Sanchez-Gonzalez 10.26.2025
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from RealtimeSTT import AudioToTextRecorder
from indextts.infer_v2 import IndexTTS2
tts = IndexTTS2(cfg_path="checkpoints/config.yaml", model_dir="checkpoints", use_fp16=False, use_cuda_kernel=False, use_deepspeed=False)



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

def handle_conversation():
    context = ""
    print("Hi! My name is Keykoe, your AI companion. How can I help you today?")
    
    while True:
        # Input via microphone
        with AudioToTextRecorder() as recorder:
            user_input = recorder.text().strip()
        print(f"You (from mic): {user_input}")

        # EXIT condition
        if user_input.lower() in ["exit", "Exit", "Goodbye", "goodbye", "quit", "Quit"]:
            goodbye_prompt = "Say a cute goodbye message and end the conversation warmly."
            result = chain.invoke({"Context": context, "Question": goodbye_prompt}).content
            print(f"Keykoe: {result.strip()}")
            text = result.content if 'result' in locals() else "Hello, I'm Keykoe, your AI companion! How can I assist you today?"
            tts.speak(text)
            break

        # Keykoe’s response
        result = chain.invoke({"Context": context, "Question": user_input})
        print(f"Keykoe: {result.strip()}")
        text = result.content if 'result' in locals() else "Hello, I'm Keykoe, your AI companion! How can I assist you today?"
        tts.speak(text)

        # Update memory (keep last 10 exchanges)
        context += f"\nHuman: {user_input}\nKeykoe: {result}"
        context = "\n".join(context.splitlines()[-20:])

if __name__ == "__main__":
    handle_conversation()
