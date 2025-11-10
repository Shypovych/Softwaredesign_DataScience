# =============================================================
#   POLYNOMIAL REGRESSION AND MODEL COMPLEXITY
# =============================================================
# This script demonstrates how polynomial degree (model complexity)
# affects regression fit quality:
#   - Low degree → underfitting (too simple)
#   - Medium degree → good fit
#   - High degree → overfitting (too flexible)

import numpy as np
import matplotlib.pyplot as plt
import warnings

# Ignore numerical warnings (e.g. poorly conditioned polynomials)
warnings.simplefilter("ignore", np.exceptions.RankWarning)

# =============================================================
#   DATA GENERATION
# =============================================================
np.random.seed(6020)  # reproducibility

m = 100  # number of samples
# x uniformly distributed in range [-3, 3]
x = 6 * np.random.rand(m) - 3
# target function: y = 0.5x² + x + 2 + noise
y = 0.5 * x**2 + x + 2 + np.random.randn(m)

# =============================================================
#   DESIGN MATRICES FOR POLYNOMIAL FITTING
# =============================================================
# np.vander(x, N) → Vandermonde matrix for polynomial degree (N-1)
# Columns: [x^(N-1), x^(N-2), ..., 1]

X1 = np.vander(x, 2)   # degree 1 (linear)
X2 = np.vander(x, 3)   # degree 2 (quadratic)
X3 = np.vander(x, 16)  # degree 15 (high complexity)

# Compute coefficients using pseudoinverse: p = (XᵀX)⁻¹ Xᵀ y
p1 = np.linalg.pinv(X1) @ y
p2 = np.linalg.pinv(X2) @ y
p3 = np.linalg.pinv(X3) @ y

# Very high degree (300) with np.polyfit (unstable but illustrative)
p4 = np.polyfit(x, y, 300)

# =============================================================
#   PREDICTIONS
# =============================================================
xf = np.arange(-3, 3, 0.1)  # dense grid for plotting
# Compute predicted y for each model
y1 = np.polyval(p1, xf)
y2 = np.polyval(p2, xf)
y3 = np.polyval(p3, xf)
y4 = np.polyval(p4, xf)

# =============================================================
#   VISUALIZATION
# =============================================================
plt.figure(figsize=(8, 5))

# Scatter of noisy observations
plt.plot(x, y, "o", color="r", label="observations", markersize=5)

# Plot each polynomial fit
plt.plot(xf, y1, label=r"$m=1$ (linear fit)")    # underfit
plt.plot(xf, y2, label=r"$m=2$ (quadratic fit)") # good fit
plt.plot(xf, y3, label=r"$m=16$ (complex fit)")  # approaching overfit
plt.plot(xf, y4, label=r"$m=300$ (overfit)")     # extreme overfit

# Formatting
plt.ylim(0, 10)
plt.xlim(-3, 3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Regression and Overfitting Demonstration")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()