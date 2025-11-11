# b8 module
import random
import math
from typing import Callable

# Function that counts how many random points fall inside the unit circle
def in_unit_circle(N: int) -> int:
    count = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            count += 1
    return count

# Modified function: estimate_pi now takes another function as argument
def estimate_pi(N: int, func: Callable[[int], int]) -> float:
    """Estimate π using a user-defined counting function."""
    M = func(N)            # call the passed function (e.g., in_unit_circle)
    return 4 * M / N       # formula π ≈ 4 * M / N

# Example usage
pi_est = estimate_pi(100000, in_unit_circle)
print(f"Estimated π ≈ {pi_est:.6f}")
print(f"Error = {abs(math.pi - pi_est):.6f}")