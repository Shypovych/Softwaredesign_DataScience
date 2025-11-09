# =============================================================
#   ATTRIBUTE DEFINITION
# =============================================================
# This stage demonstrates how to define a basic class with attributes.
# Key concept: encapsulation (data stored inside an object).

class Robot:
    """Class representing a simple robot."""

    def __init__(self, name: str, ip: list[int], port: int, speed: float) -> None:
        """Initialize robot with name, IP, port, and speed."""
        self.name = name                  # Public attribute (accessible from outside)
        self.ip = ip                      # Public attribute (IPv4 format list)
        self.__port = port                # Private attribute (hidden from outside)
        self.speed = speed                # Public attribute (float: km/h)

    def __ip2str(self) -> str:
        """Private helper converting IP list to string like '192.168.1.1'."""
        return ".".join(str(x) for x in self.ip)

    def info(self) -> str:
        """Return a simple text representation of the robot."""
        return f"{self.name} at {self.__ip2str()} speed={self.speed}"


# Create example instances
r2d2 = Robot("R2D2", [0, 0, 0, 1], 443, 32)
n5 = Robot("Number 5", [0, 0, 0, 3], 80, 20)

print("\n--- Stage 1: Attribute Definition ---")
print(r2d2.info())
print(n5.info())


# =============================================================
#   ADDING METHODS
# =============================================================
# This stage introduces methods that define object behavior.
# Key concept: methods are functions bound to the object (first arg: self).

def introduction(self) -> str:
    """Public method to describe itself using a private helper."""
    return (
        f"I am {self.name}, reachable at {self._Robot__ip2str()}, "
        f"and my top speed is {self.speed}."
    )

# Dynamically attach method to class (for educational progression)
Robot.introduction = introduction

print("\n--- Stage 2: Adding Methods ---")
print(r2d2.introduction())


# =============================================================
#   OPERATOR OVERLOADING
# =============================================================
# This stage shows how to use special (dunder) methods.
# Key concept: polymorphism — objects behave like built-in types.

def __str__(self) -> str:
    """Defines how the object is printed with print()."""
    return f"{self.name} @ {'.'.join(str(i) for i in self.ip)} (speed {self.speed})"

def __eq__(self, other: "Robot") -> bool:
    """Equality operator: compare by speed."""
    return self.speed == other.speed

def __lt__(self, other: "Robot") -> bool:
    """Less-than operator: compare speeds."""
    return self.speed < other.speed

def __add__(self, other: "Robot") -> "Robot":
    """Addition operator: merge two robots into a new one."""
    name = f"{self.name}-{other.name}"
    ip = self.ip[:-1] + [other.ip[-1]]   # combine IP parts
    port = self._Robot__port             # access private field
    speed = (self.speed + other.speed) / 2
    return Robot(name, ip, port, speed)

# Attach the new methods to Robot class
Robot.__str__ = __str__
Robot.__eq__ = __eq__
Robot.__lt__ = __lt__
Robot.__add__ = __add__

print("\n--- Stage 3: Operator Overloading ---")
print(r2d2)                        # Uses __str__()
print(n5)
print(f"r2d2 < n5 ? {r2d2 < n5}")  # Uses __lt__()
print(f"r2d2 == n5 ? {r2d2 == n5}")# Uses __eq__()
print(f"r2d2 + n5 -> {r2d2 + n5}") # Uses __add__()


# =============================================================
#   INHERITANCE EXAMPLE
# =============================================================
# This stage adds inheritance: creating specialized subclasses.
# Key concepts: inheritance, method overriding, super().

class IndustrialRobot(Robot):
    """Subclass extending Robot with payload capability."""

    def __init__(self, name, ip, port, speed, payload):
        super().__init__(name, ip, port, speed)  # Call parent constructor
        self.payload = payload                   # New attribute for payload (kg)

    def move(self) -> None:
        """Override parent's behavior with more specific message."""
        print(f"{self.name} moves carefully with {self.payload} kg payload.")


# Demonstration of inheritance
r_industrial = IndustrialRobot("WeldMaster", [192, 168, 1, 20], 9090, 25, 120)

print("\n--- Stage 4: Inheritance Example ---")
r_industrial.move()               # Overridden method
print(r_industrial.info())        # Inherited method from parent


# =============================================================
#   ABSTRACT CLASSES
# =============================================================
# This stage introduces abstract base classes (ABC).
# Key concept: enforcing interface consistency across subclasses.

from abc import ABC, abstractmethod

class FlyingTransport(ABC):
    """Abstract base class defining a flying interface."""

    @abstractmethod
    def fly(self, origin: str, destination: str, passengers: int) -> None:
        """Must be implemented by all concrete subclasses."""
        pass


class Helicopter(FlyingTransport):
    """Concrete implementation of abstract fly() method."""

    def fly(self, origin, destination, passengers):
        print(f"Helicopter flying from {origin} to {destination} with {passengers} passengers.")


class Aeroplane(FlyingTransport):
    """Another concrete subclass implementing the same interface."""

    def fly(self, origin, destination, passengers):
        print(f"Aeroplane flying from {origin} to {destination} with {passengers} passengers.")


# Demonstrate abstract class usage
print("\n--- Stage 5: Abstract Classes ---")
Helicopter().fly("INN", "QOJ", 2)
Aeroplane().fly("INN", "BER", 200)