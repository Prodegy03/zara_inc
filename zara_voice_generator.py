import sounddevice as sd
import soundfile as sf
import numpy as np
import os
from shared.logging import log

def play_intro():
    audio_path = os.path.join("C:\\", "Users", "User", "Desktop", "zara_ai", "zara_intro_voice.wav")

    if not os.path.exists(audio_path):
        log("[Zara] Intro voice file not found.")
        return

    log("[Zara] Playing intro voice...")
    try:
        # Read file with always-float32 and exact info
        data, samplerate = sf.read(audio_path, dtype='float32')
        if len(data.shape) == 1:  # Ensure mono audio has proper shape
            data = np.expand_dims(data, axis=1)

        sd.play(data, samplerate)
        sd.wait()
        log("[Zara] Intro complete.")
    except Exception as e:
        log(f"[Zara] Error playing intro: {e}")

if __name__ == "__main__":
    log("[Zara] Starting Zara system...")
    play_intro()
