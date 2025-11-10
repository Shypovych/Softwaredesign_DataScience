# =============================================================
#   STOCHASTIC GRADIENT DESCENT (SGD) WITH NUMPY
# =============================================================
# This script demonstrates linear regression using three approaches:
#   - Analytical solution via pseudoinverse
#   - Gradient Descent (GD)
#   - Stochastic Gradient Descent (SGD)
# and visualizes the difference using Matplotlib.
# -------------------------------------------------------------
# Requirements:
#   pip install numpy matplotlib
# -------------------------------------------------------------

import matplotlib.pyplot as plt
print("Matplotlib imported successfully")  # check import
import numpy as np

# =============================================================
#   INITIAL SETTINGS
# =============================================================
# Set random seed for reproducibility
np.random.seed(6020)

# Define gradient and update functions for linear regression
# Gradient of mean squared error: ∇c = 2 * Xᵀ * (Xc − y)
grad = lambda c, X, y: 2 * X.T @ (X @ c - y)
# Update rule: c ← c − δ * ∇c
update = lambda c, delta, X, y: c - delta * grad(c, X, y)

# =============================================================
#   STOCHASTIC GRADIENT DESCENT FUNCTION
# =============================================================
def sgd(c, delta, X, y, n_iter, batch_size=-1, stop=1e-10):
    """
    Perform stochastic gradient descent for linear regression.

    Args:
        c (ndarray): Initial coefficient vector (weights).
        delta (float): Learning rate (step size).
        X (ndarray): Feature matrix.
        y (ndarray): Target (output) column vector.
        n_iter (int): Number of iterations.
        batch_size (int): Number of samples per iteration (-1 = use all).
        stop (float): Convergence tolerance.

    Returns:
        ndarray: Optimized coefficients after SGD.
    """
    if batch_size == -1:
        batch_size = X.shape[0]  # use all data if not specified
    for _ in range(n_iter):
        # Randomly select subset (mini-batch)
        I = np.random.choice(X.shape[0], size=batch_size, replace=False)
        # Compute updated coefficients using the batch
        c_new = update(c, delta, X[I, :], y[I])
        # Stop early if coefficients change very little
        if np.linalg.norm(c_new - c) < stop:
            break
        c = c_new
    return c


# =============================================================
#   GRADIENT DESCENT (FULL BATCH)
# =============================================================
def gd(c, delta, X, y, n_iter, stop=1e-10):
    """Perform classic Gradient Descent (full batch version)."""
    for _ in range(n_iter):
        c_new = update(c, delta, X, y)
        if np.linalg.norm(c_new - c) < stop:
            break
        c = c_new
    return c


# =============================================================
#   SYNTHETIC DATA
# =============================================================
# Create simple 1D dataset (x, y)
x = np.arange(1, 11)
y = np.array([0.2, 0.5, 0.3, 0.5, 1.0, 1.5, 1.8, 2.0, 2.3, 2.2]).reshape((-1, 1))

# Construct feature matrix X = [x, 1]
# The second column of ones acts as the intercept term
X = np.column_stack((x, np.ones_like(x)))

# Learning parameters
delta = 0.002                   # learning rate
c_init = np.random.random((2, 1))  # random initial weights [a, b]

# =============================================================
#   TRAIN MODELS WITH DIFFERENT STRATEGIES
# =============================================================
# Run stochastic gradient descent with different batch sizes
c_10 = sgd(c_init, delta, X, y, n_iter=200, batch_size=1)   # batch of 1 (very noisy)
c_20 = sgd(c_init, delta, X, y, n_iter=200, batch_size=3)   # batch of 3 (moderate)
c_30 = sgd(c_init, delta, X, y, n_iter=200, batch_size=5)   # batch of 5 (smoother)
# Full gradient descent (deterministic)
c_ft = gd(c_20, delta, X, y, n_iter=150)
# Analytical least-squares solution (using Moore–Penrose pseudoinverse)
p_inv = np.linalg.pinv(X) @ y

# =============================================================
#   PREDICTIONS
# =============================================================
xf = np.arange(0, 11, 0.1)  # continuous range for plotting

def predict(coeffs, x_values):
    """Compute y = a*x + b using given coefficients."""
    a, b = coeffs.flatten()
    return a * x_values + b

# Compute predicted y-values for all models
y1 = predict(c_10, xf)
y2 = predict(c_20, xf)
y3 = predict(c_30, xf)
yft = predict(c_ft, xf)
y4 = predict(p_inv, xf)

# =============================================================
#   VISUALIZATION
# =============================================================
# Create a new figure
plt.figure(figsize=(8, 5))

# Plot original data points
plt.plot(x, y, "o", color="r", label="observations")

# Plot regression lines for different training methods
plt.plot(xf, y1, label=r"#I = 1 (SGD)")         # batch size 1
plt.plot(xf, y2, label=r"#I = 3 (SGD)")         # batch size 3
plt.plot(xf, yft, label=r"#I = 3 (GD, n=150)")  # full GD
plt.plot(xf, y4, label=r"Analytical $E_2$")     # least-squares result

# Configure axes, labels, and grid
plt.ylim(0, 4)
plt.xlim(0, 11)
plt.xlabel("x", fontsize=11)
plt.ylabel("y", fontsize=11)
plt.title("Stochastic Gradient Descent vs. Analytical Linear Regression", fontsize=12)
plt.legend(loc="upper left", fontsize=9)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()

# Display plot
plt.show()