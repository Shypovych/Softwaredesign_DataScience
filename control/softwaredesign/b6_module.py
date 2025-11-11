# b6 module
import random
import math

def in_unit_circle(N: int) -> int:     # N must be integer, returns integer
    count = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            count += 1
    return count

def estimate_pi(N: int) -> float:      # N must be integer, returns float
    M = in_unit_circle(N)
    return 4 * M / N

def get_accuracy(N: int) -> tuple[float, float]:
    estimated = estimate_pi(N)
    difference = abs(math.pi - estimated)
    return estimated, difference

for N in [100, 1000, 10000, 100000]:
    pi_est, error = get_accuracy(N)
    print(f"N = {N:6d} | π ≈ {pi_est:.6f} | error = {error:.6f}")

# Type hints вказують, що параметр N має бути типу int.
# Щоб підкреслити, що N завжди додатне, можна:
#   - додати коментар: N: int  # must be positive
#   - або перевірку: if N <= 0: raise ValueError("N must be positive")
# Python не примушує дотримуватися типів під час виконання —
# підказки використовуються лише інструментами перевірки типів (наприклад, mypy або VS Code).