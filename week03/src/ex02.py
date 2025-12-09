import E_Car_class

print(dir(E_Car_class))

my_new_car = E_Car_class.Car("honda", "civic", "2020")
my_e_car = E_Car_class.ElectricCar("tesla", "model S", "2022")
my_e_car.battery.read_battery_meter()
