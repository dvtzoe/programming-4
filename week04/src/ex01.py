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


def func(obj: Tomato | Apple) -> None:
    obj.type()
    obj.color()


obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato)
func(obj_apple)
