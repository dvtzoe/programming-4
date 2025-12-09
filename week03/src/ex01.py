class Car:
    def __init__(
        self,
        maker: str,
        model: str,
        year: str,
    ) -> None:
        self.maker: str = maker
        self.model: str = model
        self.year: str = year
        self.__odometer: int = 0

    def get_d_name(self) -> str:
        return f"{self.year} {self.maker} {self.model}".title()

    def read_odometer(self) -> None:
        print(f"This car has {self.__odometer} km on it!")

    def update_odometer(
        self,
        km: int,
    ) -> None:
        if km >= self.__odometer:
            self.__odometer = km
        else:
            print("You can't roll back an odometer")

    def increment_odometer(
        self,
        km: int,
    ) -> None:
        self.update_odometer(self.__odometer + km)


class Battery:
    def __init__(
        self,
        init_value: int = 80,
    ) -> None:
        self.__value: int = init_value

    def read_battery_meter(self) -> None:
        print(f"This car has {self.__value}-kWh battery.")


class ElectricCar(Car, Battery):
    def __init__(
        self,
        maker: str,
        model: str,
        year: str,
    ) -> None:
        super().__init__(maker, model, year)
        self.battery: Battery = Battery()


my_e_car = ElectricCar("tesla", "model S", "2022")
print(my_e_car.battery.read_battery_meter())
