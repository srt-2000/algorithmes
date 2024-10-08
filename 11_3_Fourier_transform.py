#origin is here
#https://proglib.io/p/preobrazovaniya-fure-dlya-obrabotki-signalov-s-pomoshchyu-python-2020-11-03

#inport libraries
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq, irfft

print("Hi, I'm the Fourier Transform algorithm.\nLet's do the transform of sound waves.\n")
#create signal
sample_rate = 44100 # frequency Hz
duration = 5        # seconds

def generate_sine_wave(freq, sample_rate_, duration_):
    x_ = np.linspace(0, duration_, sample_rate_*duration_, endpoint=False)
    frequencies = x_ * freq
    #2pi for radiant transform
    y_ = np.sin((2 * np.pi) * frequencies)
    return x_, y_

#generate 2 Hz 5 sec wave
print("First of all we create 2Hz 5 sec wave, with inlet data duration = 5, sample wave = 44100 Hz.\nLook on the figure 1, then click X.")
x, y = generate_sine_wave(2, sample_rate, duration)
#print the figure of signal
plt.plot(x, y)
plt.xlabel("Time, sec")
plt.ylabel("Frequency, Hz")
plt.suptitle('Created signal')
plt.show()

print("\nNext mixing and normalising the signals and write in into audio file.\nLook on the figure 2, then click X.\nFind the audio in this repo.")
#mixing and normalising the audio signals
_, nice_tone = generate_sine_wave(400, sample_rate, duration)
_, noise_tone = generate_sine_wave(4000, sample_rate, duration)
noise_tone = noise_tone * 0.3
mixed_tone = nice_tone + noise_tone
normalized_tone = np.int16((mixed_tone/mixed_tone.max()) * 32767)
#print the figure of mixing signal
plt.plot(normalized_tone[:1000])
plt.suptitle('Mixed and normalised signal')
plt.show()
#write signal audio
write("mysinewave.wav", sample_rate, normalized_tone)

print("\nNext we start Fourier convertion to make the signal frequency spectrum.\nLook on the figure 3, then click X.")
#Fourier convertion to make the signal frequency spectrum
N = sample_rate * duration
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1/sample_rate)
#print signal frequency spectrum
plt.plot(xf, np.abs(yf))
plt.suptitle('Signal frequency spectrum')
plt.show()

print("\nNext we make filtration of frequency spectrum.\nLook on the figure 4, then click X.")
#filtration
points_per_freq = len(xf) / (sample_rate / 2)
target_idx = int(points_per_freq * 4000)
yf[(target_idx - 2): (target_idx + 2)] = 0
#print filtration result
plt.plot(xf, np.abs(yf))
plt.suptitle('Filtered signal frequency spectrum')
plt.show()

print("\nNext we invert Fourier convertion.\nLook on the figure 5, then click X.")
#invert convertion
new_sig = irfft(yf)
#print inverted spectrum
plt.plot(new_sig[:1000])
plt.suptitle('Inverted frequency spectrum')
plt.show()