# Exercise 8.3
import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(6020)
# Parameters
N = 1024
a, b = 0, 1 / 4
t = np.linspace(a, b, N, endpoint=False)
dt = t[1] - t[0]
f1 = 50
f2 = 120
fun = lambda t: np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

f_clean = fun(t)
f_noise = fun(t) + 2.5 * np.random.randn(len(t))  # add Gaussian noise

# Manual DFT implementatipn
def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# FFT runtime
start_fft = time.time()
fhat_fft = np.fft.fft(f_noise)
fft_time = time.time() - start_fft

# DFT runtime
start_dft = time.time()
fhat_dft = DFT(f_noise)
dft_time = time.time() - start_dft

# Compare FFT and DFT
PSD_fft = np.abs(fhat_fft) ** 2 / N
PSD_dft = np.abs(fhat_dft) ** 2 / N
freq = (1 / (dt * N)) * np.arange(N)
L = np.arange(1, np.floor(N / 4), dtype="int")

# Filter based on PSD threshold
filter_mask = PSD_fft > 100
fhat_filtered = fhat_fft * filter_mask
f_filtered = np.fft.ifft(fhat_filtered)

# Figures
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
plt.plot(freq[L], PSD_fft[L], label=r"FFT")
plt.plot(freq[L], PSD_dft[L], "--", label=r"DFT")
plt.xlabel("Frequency [Hz]")
plt.ylabel("PSD")
plt.legend(loc=1)
plt.gca().set_aspect(1)

plt.figure(2)
plt.plot(t, np.real(f_filtered), label=r"Filtered (FFT)")
plt.plot(t, f_clean, label=r"Clean")
plt.xlabel("Time [s]")
plt.ylabel(r"$f$")
plt.legend(loc=1)
plt.xlim(t[0], t[-1])
plt.ylim(-5, 5)
plt.gca().set_aspect(5e-3)

# Runtime comparison
plt.figure(3)
plt.bar(["DFT", "FFT"], [dft_time, fft_time], color=["gray", "lightblue"])
plt.ylabel("Runtime [s]")
plt.title("DFT vs FFT Runtime Comparison")

plt.show()