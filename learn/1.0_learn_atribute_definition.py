# =============================================================
#   ATTRIBUTE DEFINITION
# ===============================================?=============
# This script demonstrates how to define a simple class.
# Core idea: encapsulation — store data inside objects using attributes.

class Robot:
    """Class representing a robot."""

    def __init__(self, name: str, ip: list[int], port: int, speed: float) -> None:
        """
        Initialize the robot's attributes.

        Args:
            name (str): Robot's name.
            ip (list[int]): IP address represented as a list of 4 integers.
            port (int): Network port number (kept private).
            speed (float): Robot's maximum speed.
        """
        self.name = name           # Public attribute: robot's name
        self.ip = ip               # Public attribute: list of integers (IPv4)
        self.__port = port         # Private attribute: hidden via name mangling
        self.speed = speed         # Public attribute: speed value

    def __ip2str(self) -> str:
        """Convert IP list to string format (e.g., 0.0.0.1)."""
        return ".".join(str(part) for part in self.ip)

    def info(self) -> str:
        """Return formatted description of the robot."""
        return f"I am {self.name}, reachable under {self.__ip2str()}, top speed {self.speed}."


# =============================================================
#   EXAMPLES OF OBJECT CREATION AND USAGE
# =============================================================
# Instantiate two Robot objects and print their information.

r2d2 = Robot("R2D2", [0, 0, 0, 1], 443, 32)
number5 = Robot("Number 5", [0, 0, 0, 3], 80, 20)

print("\n--- Stage 1: Attribute Definition ---")
print(r2d2.info())
print(number5.info())