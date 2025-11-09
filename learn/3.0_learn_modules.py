# ============================================================
#   MODULES — BASICS OF MODULAR PROGRAMMING
# ============================================================
# A module is simply a Python file (.py) that contains functions,
# classes, or variables which can be imported and reused.
# Key concepts: namespace, import, alias, selective import, __name__ guard.

# ============================================================
#   BUILT-IN MODULES
# ============================================================

import math  # Import the entire math module

print("\n--- Stage 1: Built-in Module ---")
print(f"Square root of 4 = {math.sqrt(4)}")   # → 2.0
print(f"Pi constant = {math.pi}")             # → 3.141592653589793


# ============================================================
#   SELECTIVE IMPORT
# ============================================================
# Import specific functions or constants from a module.

from math import sqrt, pi

print("\n--- Stage 2: Selective Import ---")
print(f"Square root of 9 = {sqrt(9)}")        # → 3.0
print(f"Pi value again = {pi}")


# ============================================================
#   MODULE ALIASING
# ============================================================
# Give a shorter or more meaningful name to a module.

import math as m

print("\n--- Stage 3: Module Aliasing ---")
print(f"Square root via alias = {m.sqrt(16)}")
print(f"Tau constant (2π) = {m.tau}")


# ============================================================
#   CUSTOM MODULE (SIMULATION)
# ============================================================
# Normally, we would create a separate file like `robot_module.py`.
# For simplicity, we simulate it here using a dynamic namespace.

print("\n--- Stage 4: Custom Module Simulation ---")

import types
robot_module = types.SimpleNamespace()  # Create a dummy module container

def say_hello(name: str) -> None:
    """Example function inside a custom module."""
    print(f"Hello, {name}! This message comes from robot_module.")

robot_module.say_hello = say_hello  # Add function to simulated module

# Use the module
robot_module.say_hello("R2D2")
robot_module.say_hello("Number 5")


# ============================================================
#   MAIN GUARD
# ============================================================
# The `__name__ == "__main__"` check prevents code from running
# automatically when this file is imported as a module.

print("\n--- Stage 5: __name__ Guard Example ---")

if __name__ == "__main__":
    print("This code runs only when executed directly (not on import).")