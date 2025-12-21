import torchaudio

waveform, sample_rate = torchaudio.load("../../Downloads/se-hatıralar.m4a")

# Gerekirse dönüştür (örneğin 16kHz'e)
resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
waveform = resampler(waveform)