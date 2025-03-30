import time
import threading
import os
from dotenv import load_dotenv
import openai

from voice.listener import VoiceListener
from voice.speaker import VoiceSpeaker
from memory.session_memory import SessionMemory
from memory.long_term_memory import store_message, find_similar_or_recent 
from shared.logging import log

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

listener = VoiceListener()
speaker = VoiceSpeaker()
memory = SessionMemory(limit=10)

log("[Zara Chat] Zara is ready for a conversation.")

def speak_in_background(text):
    thread = threading.Thread(target=speaker.speak, args=(text,))
    thread.start()

while True:
    try:
        log("[Zara Chat] Please speak now...")
        user_input = listener.listen_and_transcribe(duration=5)

        if not user_input:
            log("[Zara Chat] No input detected. Waiting...")
            continue

        log(f"[Zara Chat] You said:   {user_input}")
        memory.add("user", user_input)
        store_message("user", user_input)

        # 🔍 Try to recall related fact
        remembered = retrieve_fact(user_input)
        if remembered:
            log(f"[Zara Chat] Zara remembered:  {remembered}")
            memory.add("assistant", remembered)
            store_message("assistant", remembered)
            speak_in_background(remembered)
            continue

        # 💬 Ask GPT if no memory matched
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=memory.get(),
            temperature=0.7
        )

        zara_reply = response.choices[0].message["content"]
        log(f"[Zara Chat] Zara replies: {zara_reply}")
        memory.add("assistant", zara_reply)
        store_message("assistant", zara_reply)
        speak_in_background(zara_reply)

        time.sleep(1)

    except KeyboardInterrupt:
        log("[Zara Chat] Conversation ended by user.")
        break
    except Exception as e:
        log(f"[Zara Chat] Error: {e}")
