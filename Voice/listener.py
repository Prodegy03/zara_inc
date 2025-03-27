import whisper
import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from tempfile import NamedTemporaryFile
from shared.logging import log

class VoiceListener:
    def __init__(self, model_size="base"):
        log("[Voice] Loading Whisper model...")
        self.model = whisper.load_model(model_size)

    def listen_and_transcribe(self, duration=5, fs=16000):
        log(f"[Voice] Listening for {duration} seconds...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        with NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            wav.write(tmpfile.name, fs, recording)
            log(f"[Voice] Audio recorded to {tmpfile.name}")
            result = self.model.transcribe(tmpfile.name)
            os.remove(tmpfile.name)

        transcript = result.get("text", "").strip()
        log(f"[Voice] Transcribed text: '{transcript}'")
        return transcript
