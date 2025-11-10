# Exercise 8.1
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 2 * np.pi  # Interval
M = 5          # Nodes for the first function
M2 = 50        # Nodes for the second function
N = 512        # Interpolation points

# Hat functions
fun = lambda x, L: 0 if abs(x) > L / 4 else (1 - np.sign(x) * x * 4 / L)  # tooth-like shape
fun2 = lambda x, L: 0 if abs(x) > L / 4 else 1                            # step-like shape

# x and y for the functions
t = np.linspace(-L / 2, L / 2, N, endpoint=False)  # points for the evaluation
dt = t[1] - t[0]
w = np.pi * 2 / L

# function values
f = np.fromiter(map(lambda t_: fun(t_, L), t), t.dtype)
f2 = np.fromiter(map(lambda t_: fun2(t_, L), t), t.dtype)

# Necessary functions
scalarproduct = lambda f, g, dt: dt * np.vecdot(f, g)  # scalar product (inner product)
a_coeff = lambda n, f: 2 / L * scalarproduct(f, np.cos(w * n * t), dt)  # cosine term
b_coeff = lambda n, f: 2 / L * scalarproduct(f, np.sin(w * n * t), dt)  # sine term

# f_hat_0 
f_hat = np.zeros((M + 1, N))
f_hat[0, :] = 1 / 2 * a_coeff(0, f)  # a_0 / 2 for f
f2_hat = np.zeros((M2 + 1, N))
f2_hat[0, :] = 1 / 2 * a_coeff(0, f2)  # a_0 / 2 for f2

# Computation of the approximation
a = np.zeros(M)
b = np.zeros(M)
for i in range(M):
    a[i] = a_coeff(i + 1, f)
    b[i] = b_coeff(i + 1, f)
    f_hat[i + 1, :] = (
        f_hat[i, :] + a[i] * np.cos(w * (i + 1) * t) + b[i] * np.sin(w * (i + 1) * t)
    )

for i in range(M2):
    f2_hat[i + 1, :] = (
        f2_hat[i, :]
        + a_coeff(i + 1, f2) * np.cos(w * (i + 1) * t)
        + b_coeff(i + 1, f2) * np.sin(w * (i + 1) * t)
    )

# Figures
plt.figure(0)
plt.plot(t, f, label=r"$f$")
plt.plot(t, f_hat[-1, :], label=r"$\hat{f}_7$")
plt.xticks([])
plt.legend()
plt.gca().set_aspect(1.5)

plt.figure(1)
plt.plot(t, f_hat[0, :], label=rf"$a_{0}$")
for i in range(M):
    plt.plot(t, a[i] * np.cos(w * (i + 1) * t), label=rf"$a_{i+1}\cos({i+1}\omega t)$")
plt.legend(ncol=np.ceil((M + 1) / 2), bbox_to_anchor=(1, -0.1))
plt.xticks([])
plt.gca().set_aspect(1.5)

plt.figure(2)
plt.plot(t, f2, label=r"$f$")
plt.plot(t, f2_hat[7, :], label=r"$\hat{f}_7$")
plt.plot(t, f2_hat[20, :], label=r"$\hat{f}_{20}$")
plt.plot(t, f2_hat[50, :], label=r"$\hat{f}_{50}$")
plt.xlabel(r"$x$")
plt.legend()
plt.gca().set_aspect(1.5)

plt.show()