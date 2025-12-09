class Tomato:
    def type(self) -> None:
        print("Vegetable")

    def color(self) -> None:
        print("Red")


class Apple:
    def type(self) -> None:
        print("Fruit")

    def color(self) -> None:
        print("Red")


obj_tomato = Tomato()
obj_apple = Apple()

for plant in (obj_tomato, obj_apple):
    if getattr(plant, "__abstractmethods__", False):
        print("This is an abstract class")

    print(*dir(plant), sep=", ")
    print(str(plant.__class__).split("'")[1].split(".")[-1])
