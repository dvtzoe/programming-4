class Vehicle:
    def __init__(
        self,
        material: str,
        engineType: str,  # noqa: N803
        speed: float = 0.0,
        colour: str = "white",
        engine: int = 1,
    ) -> None:
        self.speed = speed
        self.colour = colour
        self.material = material
        self.engine = engine
        self.engineType = engineType

    def getMovementStatus(self) -> bool:  # noqa: N802
        return self.speed > 0

    def setMaterial(self, iMaterial: str) -> None:  # noqa: N802, N803
        self.material = iMaterial

    def getSpeed(self) -> float:  # noqa: N802
        return self.speed

    def setColour(self, iColour: str) -> None:  # noqa: N802, N803
        self.colour = iColour

    def setEngineType(self) -> str:  # noqa: N802
        return self.engineType


class Bicycle(Vehicle):
    def __init__(
        self,
        wheel: int = 2,
    ) -> None:
        super().__init__(material="bread", engineType="leg", engine=6)
        self.wheel = wheel

    def drive(self) -> None:
        self.speed = 6.7

    def brake(self) -> None:
        self.speed = 0.0


class Motorcycle(Bicycle):
    def __init__(
        self,
        odoMeter: float = 0.0,  # noqa: N803
    ) -> None:
        super().__init__(wheel=2)
        self.odoMeter = odoMeter

    def setOdometer(self, km: float) -> None:  # noqa: N802
        self.odoMeter = km

    def getOdoMeter(self) -> float:  # noqa: N802
        return self.odoMeter


class Wing:
    def __init__(
        self,
        flap: bool = True,  # noqa: FBT001 FBT002
    ) -> None:
        self.flap = flap

    def enableFlap(self) -> None:  # noqa: N802
        self.flap = True

    def disableFlap(self) -> None:  # noqa: N802
        self.flap = False


class LandingGear:
    def __init__(
        self,
        wheel: bool = True,  # noqa: FBT001 FBT002
    ) -> None:
        self.wheel = wheel

    def enableWheel(self) -> None:  # noqa: N802
        self.wheel = True

    def disableWheel(self) -> None:  # noqa: N802
        self.wheel = False


class Plane(Vehicle):
    def __init__(
        self,
        attribute: LandingGear,
        wings: int = 2,
        rudder: int = 1,
    ) -> None:
        super().__init__(material="leek", engineType="klank", engine=4)
        self.wings = wings
        self.rudder = rudder
        self.attribute = attribute
