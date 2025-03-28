# zara_conversation.py
import time
import os
import openai
from dotenv import load_dotenv

from voice.listener import VoiceListener
from voice.speaker import VoiceSpeaker
from shared.logging import log
from memory.session_memory import SessionMemory
from memory.long_term_memory import LongTermMemory

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Zara's modules
listener = VoiceListener()
speaker = VoiceSpeaker()
session_memory = SessionMemory()
long_term_memory = LongTermMemory()

log("[Zara Chat] Zara is ready for a conversation.")

while True:
    try:
        log("[Zara Chat] Please speak now...")
        user_input = listener.listen_and_transcribe(duration=5)

        if not user_input:
            log("[Zara Chat] No input detected. Waiting...")
            continue

        log(f"[Zara Chat] You said: {user_input}")
        session_memory.add("user", user_input)
        long_term_memory.store("user", user_input)

        # Query GPT-4 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=session_memory.get_recent(),
            temperature=0.7
        )

        zara_reply = response.choices[0].message["content"]
        log(f"[Zara Chat] Zara replies: {zara_reply}")

        session_memory.add("assistant", zara_reply)
        long_term_memory.store("assistant", zara_reply)
        speaker.speak(zara_reply)

        time.sleep(1)

    except KeyboardInterrupt:
        log("[Zara Chat] Conversation ended by user.")
        break
    except Exception as e:
        log(f"[Zara Chat] Error: {e}")
        continue
