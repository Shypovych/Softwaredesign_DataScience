# b9 module

def fibonacci(n: int) -> int:
    """Compute nth Fibonacci number using recursion."""
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

# Print first 13 Fibonacci numbers
for i in range(13):
    print(f"fibonacci({i}) = {fibonacci(i)}")