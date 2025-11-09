# =============================================================
#   PURE FUNCTION (NO SIDE-EFFECTS)
# =============================================================
# This example demonstrates a "pure function" in functional programming.
# A pure function:
#   - depends only on its input arguments,
#   - has no side effects (does not modify external state),
#   - always returns the same result for the same input.

# =============================================================
#   Function Definition
# =============================================================
def factorial(n: int) -> int:
    """
    Compute factorial of n recursively.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: The factorial of n (n!).
    """
    # Base case: factorial(0) = 1
    # Recursive case: n! = n * (n - 1)!
    return 1 if n <= 0 else n * factorial(n - 1)


# =============================================================
#   Example Usage
# =============================================================
print("\n--- Stage 1: Pure Function Example ---")
print(f"factorial(3) = {factorial(3)}")   # → 6
print(f"factorial(5) = {factorial(5)}")   # → 120
