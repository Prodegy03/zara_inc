import os
import tempfile
import sounddevice as sd
import numpy as np
import whisper
from shared.logging import log
import time
import torch

class VoiceListener:
    def __init__(self):
        log("[Voice] Loading Whisper model...")
       
        self.model = whisper.load_model("base", device="cuda" if torch.cuda.is_available() else "cpu")


    def listen_and_transcribe(self, duration=5, samplerate=16000):
        log(f"[Voice] Listening for {duration} seconds...")

        # Record from mic
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()

        # Save to temp WAV file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            filename = tmpfile.name
            # Write audio as WAV
            import soundfile as sf
            sf.write(tmpfile, recording, samplerate)

        log(f"[Voice] Audio recorded to {filename}")

        try:
            # Transcribe audio
            result = self.model.transcribe(filename)
            text = result["text"]
            log(f"[Voice] Transcription: {text}")
        finally:
            # Ensure file is deleted safely after transcription
            time.sleep(0.1)  # small delay to ensure file is not in use
            os.remove(filename)

        return text
