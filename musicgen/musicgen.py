import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# if you are in China, you need to set the endpoint to hf-mirror.com
# import os
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

model = MusicGen.get_pretrained('facebook/musicgen-melody')
model.set_generation_params(duration=20)  # generate duration seconds.

# Use the prompt generated from Five-Element Chat, or 
# use Five-Element Music Generation Prompt Reference:
# 1. earth: Create a Chinese classical piece in the Gong mode, embodying the Earth element. The music should evoke feelings of stability, peace, and harmony, reflecting the grounded and serene nature of Earth.
# 2. metal: Create a Chinese classical piece in the Shang mode, embodying the Metal element. The music should evoke feelings of strength, clarity, and precision, reflecting the sharp and resolute nature of Metal.
# 3. wood: Create a Chinese classical piece in the Jing mode, embodying the Wood element. The music should evoke feelings of vitality, growth, and creativity, reflecting the dynamic and expansive nature of Wood.
# 4. water: Create a Chinese classical piece in the Yin mode, embodying the Water element. The music should evoke feelings of fluidity, flexibility, and depth, reflecting the flowing and adaptable nature of Water.
# 5. fire: Create a Chinese classical piece in the Jing mode, embodying the Fire element. The music should evoke feelings of passion, energy, and excitement, reflecting the fiery and dynamic nature of Fire.
descriptions = ['Create a rhythmic Earth-mode piece with one instrument, featuring a unified and repetitive melody, evoking calm stability','Compose a single-instrument Earth-mode track, with a consistent, repeating melody that embodies serene stability','Compose a single-instrument Earth-mode track, with a consistent, repeating melody that embodies serene stability']

# Remeber to change the location of the input file
# Five-Element Music Reference, choose one of the following:
# 1. earth
# 2. metal
# 3. water
# 4. wood
# 5. fire
melody, sr = torchaudio.load('./earth.wav')

# generates using the melody from the given audio and the provided descriptions.
wav = model.generate_with_chroma(descriptions, melody[None].expand(3, -1, -1), sr)

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness")
