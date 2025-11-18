# Exercise 8.5
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

c = 2
a, b = -20, 20
L = b - a
N = 1000
x = np.linspace(a, b, N, endpoint=False)
dx = x[1] - x[0]

# Define discrete wave numbers
kappa = 2 * np.pi * np.fft.fftfreq(N, d=dx)   # added missing Fourier wavenumbers

# Initial condition
u0 = 1 / np.cosh(x)
u0hat = np.fft.fft(u0)

# SciPy's odeint function doesn't play well with complex numbers,
# so we recast the state u0hat from an N-element complex vector
# to a 2N-element real vector
u0hat_ri = np.concatenate((u0hat.real, u0hat.imag))

# Simulate in Fourier frequency domain
dt = 0.025
T = np.arange(0, 600 * dt, dt)


def rhsWave(uhat_ri, t, kappa, c):
    uhat = uhat_ri[:N] + (1j) * uhat_ri[N:]
    d_uhat = -1j * c * kappa * uhat   # added Fourier–space derivative for advection
    d_uhat_ri = np.concatenate((d_uhat.real, d_uhat.imag)).astype("float64")
    return d_uhat_ri


uhat_ri = odeint(rhsWave, u0hat_ri, T, args=(kappa, c))

uhat = uhat_ri[:, :N] + (1j) * uhat_ri[:, N:]

u = np.zeros_like(uhat)

for k in range(len(T)):
    u[k, :] = np.fft.ifft(uhat[k, :])

u = u.real

# Waterfall plot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$t$")
ax.set_zlabel(r"$u(t, x)$")
ax.set_zticks([])
u_plot = u[0:-1:60, :]
for j in range(u_plot.shape[0]):
    ys = j * np.ones(u_plot.shape[1])
    ax.plot(x, ys, u_plot[j, :])

# Image plot
plt.figure()
plt.imshow(np.flipud(u), aspect=1.5)
plt.xlabel(r"$x$")
plt.ylabel(r"$t \to$")
plt.gca().axes.get_xaxis().set_ticks([])
plt.gca().axes.get_yaxis().set_ticks([])
plt.show()