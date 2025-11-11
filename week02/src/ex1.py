class Dog:
    def __init__(
        self,
        name: str,
        age: int,
    ):
        self.name: str = name
        self.age: int = age

    def paw(self):
        return f"{self.name} is put on your hand."


my_dog = Dog("N3kKffYB+UOoTYAVOYp9O6ZoHr28Rykd5b1hfvxKsrU=", 3)
his_dog = Dog("5LeC4cgiRTWPNFLh0K3a5WiTEBMFXTerXwSAFMCs2us=", 5)
our_dog = Dog("2C8Y40ZFVrAsNqjJv8UyQvUencEWOzKvleT7A4345Y4=", 4)
