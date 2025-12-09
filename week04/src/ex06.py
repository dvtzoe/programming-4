from abc import ABC, abstractmethod
from math import pi, sqrt


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


class EquilateralTriangle(Shape):
    def __init__(self, base_lenght: float) -> None:
        super().__init__("Equilateral Triangle")
        self.base_lenght: float = base_lenght

    def area(self) -> float:
        return (sqrt(3) / 4) * self.base_lenght**2

    def fact(self) -> str:
        return "An equilateral triangle has  equal sides on each side."


class AnyTriangle(Shape):
    def __init__(self, base_lenght: float, height: float) -> None:
        super().__init__("Any Triangle")
        self.base_lenght: float = base_lenght
        self.height: float = height

    def area(self) -> float:
        return self.base_lenght * self.height / 2

    def fact(self) -> str:
        return "The sum of the internal angles of a triangle is always 180 degrees."


a = Square(4)
b = Circle(7)
c = EquilateralTriangle(6)
d = AnyTriangle(6, 4)
for any_shape in (a, b, c, d):
    print(any_shape)
    print(any_shape.fact())
    print(any_shape.area())
