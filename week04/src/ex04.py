from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def area(self) -> float:
        pass

    def fact(self) -> str:
        return "I am a two-dimensional shape."

    def __str__(self) -> str:
        return self.name


class Square(Shape):
    def __init__(self, length: float) -> None:
        super().__init__("Square")
        self.length: float = length

    def area(self) -> float:
        return self.length**2

    def fact(self) -> str:
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius: float = radius

    def area(self) -> float:
        return pi * self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
