# zara_conversation.py
import time
from voice.listener import VoiceListener
from voice.speaker import VoiceSpeaker
from shared.logging import log
import openai
from dotenv import load_dotenv
import openai
import os

load_dotenv()  # Loads the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = []

listener = VoiceListener()
speaker = VoiceSpeaker()

log("[Zara Chat] Zara is ready for a conversation.")

while True:
    try:
        log("[Zara Chat] Please speak now...")
        user_input = listener.listen_and_transcribe(duration=5)

        if not user_input:
            log("[Zara Chat] No input detected. Waiting...")
            continue

        log(f"[Zara Chat] You said: {user_input}")
        conversation_history.append({"role": "user", "content": user_input})

        # Query GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history[-10:],  # keep only the last 10 exchanges for context
            temperature=0.7
        )

        zara_reply = response.choices[0].message["content"]
        log(f"[Zara Chat] Zara replies: {zara_reply}")

        conversation_history.append({"role": "assistant", "content": zara_reply})
        speaker.speak(zara_reply)

        time.sleep(1)

    except KeyboardInterrupt:
        log("[Zara Chat] Conversation ended by user.")
        break
    except Exception as e:
        log(f"[Zara Chat] Error: {e}")
        continue
