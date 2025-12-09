# Import required modules
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand: str, model: str, year: str) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: str = year

    # Create abstract method
    @abstractmethod
    def print_details(self) -> None:
        pass

    # Create concrete method
    def accelerate(self) -> None:
        print("speed up ...")

    def break_applied(self) -> None:
        print("Car stop")


# Create child class
class Hatchback(Car):
    def print_details(self) -> None:
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self) -> None:
        print("Not having this feature")


class Suv(Car):
    def print_details(self) -> None:
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def four_wheel_drive(self) -> None:
        print("Available")


car1: Car = Hatchback("Maruti", "Alto", "2022")

car1.print_details()
car1.accelerate()
