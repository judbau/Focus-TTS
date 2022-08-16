import librosa
import numpy as np
from glob import glob
import os
from scipy.io.wavfile import write

wavs = glob("/data/s4954475/DeepLearningExamples/PyTorch/SpeechSynthesis/FastPitch/prosody-control/wavs/*.wav")

for file in wavs:
  audio, sr = librosa.load(file, sr = 22050)
  path = os.path.basename(file)
  write(f"/data/s4954475/DeepLearningExamples/PyTorch/SpeechSynthesis/FastPitch/prosody-control/wavs_converted/{path}", sr, audio)