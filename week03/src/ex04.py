from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(
        self,
        age: int,
        weight: float,
        gender: str,
    ):
        self.age: int = age
        self.weight: float = weight
        self.gender: str = gender

    @abstractmethod
    def show_info(self):
        pass


class Dog(Pet):
    def __init__(
        self,
        age: int,
        weight: float,
        gender: str,
        fang_size: float,
    ):
        super().__init__(age, weight, gender)
        self.fang_size: float = fang_size

    def show_info(self):
        print(
            f"Dog - Age: {self.age}, Weight: {self.weight}, Gender: {self.gender}, Fang Size: {self.fang_size}"
        )


class Cat(Pet):
    def __init__(
        self,
        age: int,
        weight: float,
        gender: str,
        fang_size: float,
    ):
        super().__init__(age, weight, gender)
        self.fang_size: float = fang_size

    def show_info(self):
        print(
            f"Cat - Age: {self.age}, Weight: {self.weight}, Gender: {self.gender}, Fang Size: {self.fang_size}"
        )


class Bird(Pet):
    def __init__(
        self,
        age: int,
        weight: float,
        gender: str,
        wing_size: float,
    ):
        super().__init__(age, weight, gender)
        self.wing_size: float = wing_size

    def show_info(self):
        print(
            f"Bird - Age: {self.age}, Weight: {self.weight}, Gender: {self.gender}, Wing Size: {self.wing_size}"
        )
