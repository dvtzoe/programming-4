class Bird:
    def intro(self) -> None:
        print("There are many types of birds.")

    def flight(self) -> None:
        print("birds can fly.")


class Sparrow(Bird):
    def flight(self) -> None:
        print("Sparrows can fly.")


class Ostrich(Bird):
    pass
    # def flight(self) -> None:
    #     print("Ostriches cannot fly.")


obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_sparrow.intro()
obj_sparrow.flight()

obj_ostrich.intro()
obj_ostrich.flight()
