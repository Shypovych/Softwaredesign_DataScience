# ============================================================
#   PACKAGES — ORGANIZING MODULES
# ============================================================
# A package is a directory that contains several related modules.
# It must contain an __init__.py file to be recognized as a package.
# Goal: organize code, avoid name conflicts, and improve maintainability.

# ============================================================
#   PACKAGE STRUCTURE (THEORY)
# ============================================================
# Example:
# mypackage/
# ├── __init__.py
# ├── operations.py
# └── geometry.py
#
# operations.py  → defines basic math functions
# geometry.py    → defines shape functions
#
# Import examples:
#   import mypackage.operations
#   from mypackage.geometry import area_rectangle

print("\n--- Stage 1: Package Structure Overview ---")
print("mypackage/")
print(" ├── __init__.py")
print(" ├── operations.py")
print(" └── geometry.py")


# ============================================================
#   SIMULATION OF PACKAGE MODULES
# ============================================================
# To demonstrate, we simulate two modules from a package.

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b

def area_rectangle(width: float, height: float) -> float:
    """Compute area of a rectangle."""
    return width * height

def perimeter_rectangle(width: float, height: float) -> float:
    """Compute perimeter of a rectangle."""
    return 2 * (width + height)


# ============================================================
#   USING PACKAGE MODULES
# ============================================================
# Demonstrate calling functions as if they were imported from a package.

print("\n--- Stage 3: Package Simulation ---")
print(f"Addition 3 + 5 = {add(3, 5)}")                     # → 8
print(f"Subtraction 10 - 4 = {subtract(10, 4)}")           # → 6
print(f"Area of 4×6 rectangle = {area_rectangle(4, 6)}")   # → 24
print(f"Perimeter of 4×6 rectangle = {perimeter_rectangle(4, 6)}")  # → 20


# ============================================================
#   __init__.py FILE
# ============================================================
# The __init__.py file allows to define what gets exposed
# when the package is imported. For example:
#
# __all__ = ["operations", "geometry"]
#
# This controls what can be imported via `from mypackage import *`.

print("\n--- Stage 4: Role of __init__.py ---")
print("Defines package exports and initialization logic.")