import os
import sounddevice as sd
import numpy as np
import torch
from TTS.api import TTS
from shared.logging import log

class VoiceSpeaker:
    def __init__(self, voice_model="tts_models/multilingual/multi-dataset/xtts_v2"):
        log("[Voice] Loading TTS model...")
        self.tts = TTS(voice_model, gpu=torch.cuda.is_available())

    def speak(self, text):
        if not text:
            log("[Voice] No text to speak.")
            return
        log(f"[Voice] Speaking: '{text}'")
        wav = self.tts.tts(text=text, speaker_wav=None, language="en")
        wav_np = np.array(wav, dtype=np.float32)
        sd.play(wav_np, samplerate=24000)
        sd.wait()
