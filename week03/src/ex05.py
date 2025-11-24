from __future__ import annotations


class EnginePowered:
    horsepower: int | None
    fuel_type: str | None
    running: bool

    def __init__(
        self,
        *,
        horsepower: int | None = None,
        fuel_type: str | None = None,
        number_of_wheels: int | None = None,
        brand: str | None = None,
        color: str | None = None,
    ) -> None:
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False

    def start_engine(self) -> None:
        self.running = True
        print("Engine started.")


class WheeledVehicle:
    number_of_wheels: int | None
    brand: str | None
    color: str | None

    def __init__(
        self,
        *,
        horsepower: int | None = None,
        fuel_type: str | None = None,
        number_of_wheels: int | None = None,
        brand: str | None = None,
        color: str | None = None,
    ) -> None:
        self.number_of_wheels = number_of_wheels
        self.brand = brand
        self.color = color

    def drive(self) -> None:
        print(f"{self.brand} is driving on {self.number_of_wheels} wheels.")


class Car(EnginePowered, WheeledVehicle):
    seats: int
    model: str
    year: int

    def __init__(
        self,
        horsepower: int,
        fuel_type: str,
        number_of_wheels: int,
        brand: str,
        color: str,
        seats: int,
        model: str,
        year: int,
    ) -> None:
        super().__init__(
            horsepower=horsepower,
            fuel_type=fuel_type,
            number_of_wheels=number_of_wheels,
            brand=brand,
            color=color,
        )
        self.seats = seats
        self.model = model
        self.year = year


class Motorcycle(EnginePowered, WheeledVehicle):
    has_sidecar: bool
    torque: int
    style: str

    def __init__(
        self,
        horsepower: int,
        fuel_type: str,
        number_of_wheels: int,
        brand: str,
        color: str,
        has_sidecar: bool,
        torque: int,
        style: str,
    ) -> None:
        super().__init__(
            horsepower=horsepower,
            fuel_type=fuel_type,
            number_of_wheels=number_of_wheels,
            brand=brand,
            color=color,
        )
        self.has_sidecar = has_sidecar
        self.torque = torque
        self.style = style


class Truck(EnginePowered, WheeledVehicle):
    max_load: int
    bed_length: float
    drivetrain: str

    def __init__(
        self,
        horsepower: int,
        fuel_type: str,
        number_of_wheels: int,
        brand: str,
        color: str,
        max_load: int,
        bed_length: float,
        drivetrain: str,
    ) -> None:
        super().__init__(
            horsepower=horsepower,
            fuel_type=fuel_type,
            number_of_wheels=number_of_wheels,
            brand=brand,
            color=color,
        )
        self.max_load = max_load
        self.bed_length = bed_length
        self.drivetrain = drivetrain
