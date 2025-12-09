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


my_new_car = Car("Honda", "Civic", "2020")
my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-150)
my_new_car.read_odometer()
