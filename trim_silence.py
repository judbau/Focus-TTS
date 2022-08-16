from pydub import AudioSegment
import os

def detect_leading_silence(wav, silence_threshold=-30.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while wav[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(wav):
        trim_ms += chunk_size

    return trim_ms

directory = "/data/s4954475/DeepLearningExamples/PyTorch/SpeechSynthesis/FastPitch/prosody-control/wavs/"

for wav in os.listdir(directory):
  print(wav)
  if wav.endswith(".wav"):
    fullpath = "/data/s4954475/DeepLearningExamples/PyTorch/SpeechSynthesis/FastPitch/prosody-control/wavs/" + wav
    sound = AudioSegment.from_file(fullpath)
    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]

    trimmed_sound.export("/data/s4954475/DeepLearningExamples/PyTorch/SpeechSynthesis/FastPitch/prosody-control/wavs/trimmed/" + wav, format="wav")
    continue
  else:
    continue