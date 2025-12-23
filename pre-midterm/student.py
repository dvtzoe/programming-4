class Student:
    def __init__(
        self,
        studentId: int,  # noqa: N803
        firstName: str,  # noqa: N803
        lastName: str,  # noqa: N803
        age: int,
    ) -> None:
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def showInfo(self) -> None:  # noqa: N802
        print("Info")


miku = Student(39, "Miku", "Hatsune", 16)
miku.showInfo()
