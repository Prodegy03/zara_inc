from listener import VoiceListener
from speaker import VoiceSpeaker

def run_voice_test():
    print("\n[Zara Test] Initializing voice interface...")
    listener = VoiceListener()
    speaker = VoiceSpeaker()

    print("[Zara Test] Please speak now...")
    text = listener.listen_and_transcribe(duration=5)

    if text:
        print(f"[Zara Test] You said: {text}")
        speaker.speak(f"You said: {text}")
    else:
        print("[Zara Test] Nothing was captured.")

if __name__ == "__main__":
    run_voice_test()
