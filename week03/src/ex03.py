from abc import ABC, abstractmethod


class Bee(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

    def attack(self) -> None:
        print("Attack against an intruder")


class HoneyBee(Bee):
    def fly(self) -> None:
        print("Looking for feed")


class HornetBee(Bee):
    def fly(self) -> None:
        print("Looking for enemy")


# # (1)
# bee = Bee()
# # (2)
# hb: bee = HoneyBee()
# hb.fly()
# hb.attack()
# # (3)
# hb: bee = HornetBee()
# hb.fly()
# hb.attack()
