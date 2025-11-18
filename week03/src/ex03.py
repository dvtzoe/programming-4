from abc import ABC, abstractmethod


class bee(ABC):
    @abstractmethod
    def fly(self):
        pass

    def attack(self):
        print("Attack against an intruder")


class honey_bee(bee):
    def fly(self):
        print("Looking for feed")


class hornet_bee(bee):
    def fly(self):
        print("Looking for enemy")


# # (1)
# bee = bee()
# # (2)
# hb: bee = honey_bee()
# hb.fly()
# hb.attack()
# # (3)
# hb: bee = hornet_bee()
# hb.fly()
# hb.attack()
