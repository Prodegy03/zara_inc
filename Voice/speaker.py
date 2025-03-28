import os
import sounddevice as sd
import numpy as np
import torch
from TTS.api import TTS
from shared.logging import log

# Patch: Allow deserialization of custom classes used in XTTS v2
from torch.serialization import safe_globals
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig

class VoiceSpeaker:
    def __init__(self, voice_model="tts_models/multilingual/multi-dataset/xtts_v2"):
        log("[Voice] Loading TTS model...")

        with safe_globals([XttsConfig, XttsAudioConfig]):
            self.tts = TTS(voice_model, gpu=torch.cuda.is_available())

        # Ensure Zara's cloned voice sample exists
        self.sample_voice_path = os.path.join("voice", "zara_voice_sample.wav")
        if not os.path.exists(self.sample_voice_path):
            raise FileNotFoundError(f"Missing speaker WAV file: {self.sample_voice_path}")

    def speak(self, text):
        if not text:
            log("[Voice] No text to speak.")
            return

        log(f"[Voice] Speaking: '{text}'")

        wav = self.tts.tts(
            text=text,
            speaker_wav=self.sample_voice_path,
            language="en"
        )

        wav_np = np.array(wav, dtype=np.float32)
        sd.play(wav_np, samplerate=24000)
        sd.wait()
