import torchaudio

waveform, sample_rate = torchaudio.load("giris.mp3")

# Gerekirse dönüştür (örneğin 16kHz'e)
resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
waveform = resampler(waveform)