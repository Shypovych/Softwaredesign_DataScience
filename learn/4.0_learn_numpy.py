# =============================================================
#   NUMPY PERFORMANCE — SCALAR PRODUCT COMPARISON
# =============================================================
# This script compares a pure Python loop implementation
# of the scalar (dot) product with NumPy’s vectorized version.
# Goal: illustrate speed advantage of vectorized computation.

import random
import timeit
import numpy as np

# =============================================================
#   Generate Random Data
# =============================================================
random.seed(42)
min_value, max_value = 1, 100

# Create two lists with 1,000,000 random integers each
a = [random.randint(min_value, max_value) for _ in range(1_000_000)]
b = [random.randint(min_value, max_value) for _ in range(1_000_000)]

# =============================================================
#   Pure Python Implementation
# =============================================================
def dot(a: list[int], b: list[int]) -> int:
    """Compute scalar product using a Python loop."""
    r = 0
    for first, second in zip(a, b):
        r += first * second
    return r

# Measure time for 1000 repetitions
t1 = timeit.timeit(lambda: dot(a, b), number=1000)

# =============================================================
#   NumPy Vectorized Implementation
# =============================================================
np_a = np.array(a, dtype=np.int64)
np_b = np.array(b, dtype=np.int64)

# NumPy’s built-in dot product (vectorized)
t2 = timeit.timeit(lambda: np.vdot(np_a, np_b), number=1000)

# =============================================================
#   Comparison Results
# =============================================================
loop_result = dot(a, b)
numpy_result = np.vdot(np_a, np_b)
speedup = t1 / t2

print("\n--- Stage 1: Scalar Product Performance Comparison ---")
print(f"loop result = {loop_result}, time = {t1:.6f} s")
print(f"numpy result = {numpy_result}, time = {t2:.6f} s")
print(f"Speedup factor = {speedup:.2f}× faster with NumPy")

# Example output (depends on system performance):
# loop result 2550205506, time t1 = 53.5093
# numpy result 2550205506, time t2 = 0.6156
# Speedup 86.9×