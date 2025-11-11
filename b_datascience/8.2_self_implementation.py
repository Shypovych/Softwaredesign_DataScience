# Exercise 8.2
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(6020)
# Parameters
N = 1024
a, b = 0, 1 / 4
t = np.linspace(a, b, N, endpoint=False)  # time samples
dt = t[1] - t[0]
f1 = 50
f2 = 120
fun = lambda t: np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)  # signal with 2 frequencies

f_clean = fun(t)
f_noise = fun(t) + 2.5 * np.random.randn(len(t))  # noisy version of signal

fhat_noise = np.fft.fft(f_noise)  # Fourier transform of noisy signal
fhat_clean = np.fft.fft(f_clean)  # Fourier transform of clean signal

PSD_noise = np.abs(fhat_noise) ** 2 / N  # power spectral density of noisy signal
PSD_clean = np.abs(fhat_clean) ** 2 / N  # power spectral density of clean signal

freq = (1 / (dt * N)) * np.arange(N)
L = np.arange(1, np.floor(N / 4), dtype="int")

# Filtering in the frequency domain
filter = freq < 100  # allow frequencies below 100 Hz
PSDclean = PSD_noise * filter  # zero out the rest of the spectrum
fhat_filtered = fhat_noise * filter  # apply filter to FFT coefficients
f_filtered = np.fft.ifft(fhat_filtered)  # inverse FFT to recover filtered signal

# Plots
plt.figure(0)
plt.plot(t, f_noise, ":", label=r"Noisy")
plt.plot(t, f_clean, label=r"Clean")
plt.xlabel("Time [s]")
plt.ylabel(r"$f$")
plt.xlim(t[0], t[-1])
plt.ylim(-5, 5)
plt.legend(loc=1)
plt.gca().set_aspect(5e-3)

plt.figure(1)
plt.plot(freq[L], PSD_noise[L], label=r"Noisy")
plt.plot(freq[L], PSD_clean[L], label=r"Clean")
plt.xlabel("Frequency [Hz]")
plt.ylabel("PSD")
plt.xlim(0, int(freq[L[-1] + 1]))
plt.legend(loc=1)
plt.gca().set_aspect(1)

plt.figure(3)
plt.plot(t, np.real(f_filtered), label=r"Filtered")
plt.plot(t, f_clean, label=r"Clean")
plt.xlabel("Time [s]")
plt.ylabel(r"$f$")
plt.xlim(t[0], t[-1])
plt.ylim(-5, 5)
plt.legend(loc=1)
plt.gca().set_aspect(5e-3)
plt.show()