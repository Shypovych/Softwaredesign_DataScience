# b5 module
import random
import math

# Function that counts how many random points fall inside the unit circle
def in_unit_circle(N):
    count = 0
    for _ in range(N):
        x, y = random.random(), random.random()          # random coordinates in [0,1]
        if x**2 + y**2 <= 1:                             # inside quarter circle
            count += 1
    return count                                         # M value — points inside circle

# Function that estimates π using Equation B.1: π ≈ 4 * M / N
def estimate_pi(N):
    M = in_unit_circle(N)
    return 4 * M / N

# Function that measures accuracy of estimation
def get_accuracy(N):
    estimated = estimate_pi(N)
    difference = abs(math.pi - estimated)
    return estimated, difference

# Different sample sizes simulation
for N in [100, 1000, 10000, 100000]:
    pi_est, error = get_accuracy(N)
    print(f"N = {N:6d} | π ≈ {pi_est:.6f} | error = {error:.6f}")