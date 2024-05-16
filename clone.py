import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS

# Great accuracy

tts = TTS("tts_models/en/vctk/vits").to(device)
tts.tts_to_file(text="Waddle waddle! Hiya! I'm Pebble the Penguin! What's up? Want to explore some Lush products with me?", speaker="p241", file_path="output_2.wav")

#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
#tts.tts_to_file(text="Waddle waddle! Hiya! I'm Pebble the Penguin! What's up? Want to explore some Lush products with me?", speaker_wav=c:\tmp\mark.wav, file_path="output.wav", language="en", split_sentences=False)

