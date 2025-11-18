class Car:
    def __init__(
        self,
        maker: str,
        model: str,
        year: str,
    ):
        self.maker: str = maker
        self.model: str = model
        self.year: str = year
        self.__odometer: int = 0

    def get_d_name(self):
        return f"{self.year} {self.maker} {self.model}".title()

    def read_odometer(self):
        print(f"This car has {self.__odometer} km on it!")

    def update_odometer(
        self,
        km: int,
    ):
        if km >= self.__odometer:
            self.__odometer = km
        else:
            print("You can't roll back an odometer")

    def increment_odometer(
        self,
        km: int,
    ):
        self.update_odometer(self.__odometer + km)


class Battery:
    def __init__(
        self,
        init_value: int = 80,
    ):
        self.__value: int = init_value

    def read_battery_meter(self):
        print(f"This car has {self.__value}-kWh battery.")


class ElectricCar(Car, Battery):
    def __init__(
        self,
        maker: str,
        model: str,
        year: str,
    ):
        super().__init__(maker, model, year)
        self.battery: Battery = Battery()


my_E_car = ElectricCar("tesla", "model S", "2022")
print(my_E_car.battery.read_battery_meter())
