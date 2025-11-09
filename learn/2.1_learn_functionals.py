# ============================================================
#   FUNCTIONAL PROGRAMMING BASICS
# ============================================================
# This script demonstrates key functional programming tools:
#   - lambda (anonymous functions)
#   - map() (apply function to all elements)
#   - filter() (select elements that meet a condition)
#   - reduce() (aggregate iterable into a single value)
# Concepts: immutability, function composition, higher-order functions.

from functools import reduce
from operator import mul, add


# ============================================================
#   LAMBDA (Anonymous Function)
# ============================================================
# A lambda is a short, anonymous function useful for small tasks.

square = lambda a: a ** 2  # Inline function to square a number

print("\n--- Stage 1: Lambda Examples ---")
print(f"square(2) = {square(2)}")    # → 4
print(f"square(-1) = {square(-1)}")  # → 1


# ============================================================
#   MAP
# ============================================================
# The map() function applies a given function to each item in an iterable.

print("\n--- Stage 2: Map Examples ---")
iterator = map(square, range(1, 5))  # Applies square() to [1, 2, 3, 4]
print(list(iterator))  # → [1, 4, 9, 16]


# ============================================================
#   FILTER
# ============================================================
# The filter() function filters elements of an iterable using a predicate.

print("\n--- Stage 3: Filter Examples ---")
is_even = lambda x: x % 2 == 0       # Returns True for even numbers
even_numbers = filter(is_even, range(10))
print(list(even_numbers))  # → [0, 2, 4, 6, 8]


# ============================================================
#   REDUCE
# ============================================================
# The reduce() function aggregates all elements into a single value.
# It repeatedly applies a binary function (e.g., add or multiply).

print("\n--- Stage 4: Reduce Examples ---")

def factorial_reduce(n: int) -> int:
    """Compute factorial using reduce and multiplication."""
    return reduce(mul, range(1, n + 1), 1)  # '1' is the initial value

print(f"factorial_reduce(3) = {factorial_reduce(3)}")  # → 6
print(f"factorial_reduce(5) = {factorial_reduce(5)}")  # → 120

# Reduce can also sum numbers
result = reduce(add, [1, 2, 3], 100)  # start with 100
print(f"Sum with initial value: {result}")  # → 106


# ============================================================
#   COMBINING FUNCTIONS
# ============================================================
# Example combining map(), filter(), and reduce() in one expression.
# This is called "function composition".

print("\n--- Stage 5: Combined Usage ---")

numbers = range(1, 6)  # 1..5
# Square only even numbers, then sum them up
sum_even_squares = reduce(add, map(square, filter(is_even, numbers)), 0)
print(f"Sum of even squares from 1 to 5: {sum_even_squares}")  # → 20