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
        self.odometer: int = 0

    def get_d_name(self):
        return f"{self.year} {self.maker} {self.model}".title()

    def read_odometer(self):
        print(f"This car has {self.odometer} km on it!")


my_new_car = Car("Honda", "Civic", "2020")
my_new_car.odometer = 23
my_new_car.read_odometer()
