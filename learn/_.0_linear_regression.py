# =============================================================
#   ROBUST LINEAR REGRESSION WITH DIFFERENT ERROR NORMS
# =============================================================
# This script demonstrates how different cost functions (L∞, L₁, L₂)
# influence linear regression results and how they react to outliers.
#
# It compares:
#   - Chebyshev norm  (L∞)  → minimizes maximum deviation
#   - Manhattan norm  (L₁)  → robust to outliers
#   - Euclidean norm  (L₂)  → least squares (standard)
#   - Analytical solution (pseudoinverse)
#
# -------------------------------------------------------------
# Requirements:
#   pip install numpy matplotlib scipy
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# =============================================================
#   COST FUNCTION DEFINITIONS
# =============================================================

def fit_Linf(x0, t):
    """L∞ norm: minimize maximum absolute deviation."""
    x, y = t
    return 1 / len(y) * np.max(np.abs(x0[0] * x + x0[1] - y))

def fit_L1(x0, t):
    """L₁ norm: minimize sum of absolute deviations (robust)."""
    x, y = t
    return 1 / len(y) * np.sum(np.abs(x0[0] * x + x0[1] - y))

def fit_L2(x0, t):
    """L₂ norm: minimize sum of squared deviations (least squares)."""
    x, y = t
    return 1 / len(y) * np.sum((x0[0] * x + x0[1] - y) ** 2)


# =============================================================
#   SYNTHETIC DATA
# =============================================================
# Dataset without outlier
x = np.arange(1, 11)
y = np.array([0.2, 0.5, 0.3, 0.5, 1.0, 1.5, 1.8, 2.0, 2.3, 2.2])

# Same dataset, but with one strong outlier (at x=4)
z = np.array([0.2, 0.5, 0.3, 3.5, 1.0, 1.5, 1.8, 2.0, 2.3, 2.2])

# Group data for optimization
t1 = (x, y)
t2 = (x, z)

# Initial parameter guess for line y = a*x + b
x0 = np.array([1.0, 1.0])


# =============================================================
#   OPTIMIZATION USING SCIPY.FMIN
# =============================================================
# Find best [a, b] coefficients by minimizing each cost function
p_Linf = scipy.optimize.fmin(fit_Linf, x0, args=(t1,), disp=False)
p_L1   = scipy.optimize.fmin(fit_L1,   x0, args=(t1,), disp=False)
p_L2   = scipy.optimize.fmin(fit_L2,   x0, args=(t1,), disp=False)

# Repeat for dataset containing outlier
p_Linf_out = scipy.optimize.fmin(fit_Linf, x0, args=(t2,), disp=False)
p_L1_out   = scipy.optimize.fmin(fit_L1,   x0, args=(t2,), disp=False)
p_L2_out   = scipy.optimize.fmin(fit_L2,   x0, args=(t2,), disp=False)


# =============================================================
#   ANALYTICAL SOLUTION (LEAST SQUARES)
# =============================================================
# Using pseudoinverse: p = (XᵀX)⁻¹ Xᵀ y
X = np.column_stack((x, np.ones_like(x)))  # features [x, 1]
p_pinv_y = np.linalg.pinv(X) @ y
p_pinv_z = np.linalg.pinv(X) @ z


# =============================================================
#   PREDICTIONS FOR PLOTTING
# =============================================================
xf = np.arange(0, 11, 0.1)  # dense range for smooth lines

# Model evaluation (y = a*x + b)
y_Linf = np.polyval(p_Linf, xf)
y_L1   = np.polyval(p_L1, xf)
y_L2   = np.polyval(p_L2, xf)
y_pinv = np.polyval(p_pinv_y, xf)

# Same for dataset with outlier
y_Linf_out = np.polyval(p_Linf_out, xf)
y_L1_out   = np.polyval(p_L1_out, xf)
y_L2_out   = np.polyval(p_L2_out, xf)
y_pinv_out = np.polyval(p_pinv_z, xf)


# =============================================================
#   VISUALIZATION
# =============================================================
plt.figure(figsize=(7, 6))

# -------------------------------------------------------------
# (a) Original dataset (no outlier)
plt.subplot(2, 1, 1)
plt.plot(x, y, "o", color="r", label="observations")
plt.plot(xf, y_Linf, label=r"$E_\infty$  (max abs error)")
plt.plot(xf, y_L1, "--", linewidth=2, label=r"$E_1$  (abs sum)")
plt.plot(xf, y_L2, "-.", linewidth=2, label=r"$E_2$  (squared sum)")
plt.plot(xf, y_pinv, ":", linewidth=2, label=r"$X^\dagger$  (pseudo-inverse)")
plt.ylim(0, 4)
plt.xlim(0, 11)
plt.legend(loc="upper left", fontsize=9)
plt.title("Linear fitting without outlier")
plt.grid(True, linestyle="--", alpha=0.7)
plt.gca().set_aspect(1)

# -------------------------------------------------------------
# (b) Dataset with outlier
plt.subplot(2, 1, 2)
plt.plot(x, z, "o", color="r", label="observations (with outlier)")
plt.plot(xf, y_Linf_out, label=r"$E_\infty$")
plt.plot(xf, y_L1_out, "--", linewidth=2, label=r"$E_1$")
plt.plot(xf, y_L2_out, "-.", linewidth=2, label=r"$E_2$")
plt.plot(xf, y_pinv_out, ":", linewidth=2, label=r"$X^\dagger$")
plt.ylim(0, 4)
plt.xlim(0, 11)
plt.legend(loc="upper left", fontsize=9)
plt.title("Linear fitting with outlier (robustness comparison)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.gca().set_aspect(1)

plt.tight_layout()
plt.show()