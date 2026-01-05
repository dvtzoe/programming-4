class Student:
    def __init__(
        self,
        studentId: int | None,  # noqa: N803
        firstName: str,  # noqa: N803
        lastName: str,  # noqa: N803
        age: int,
    ) -> None:
        self.studentId = studentId or 0
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def showInfo(self) -> None:  # noqa: N802
        print(f"""studentId: {self.studentId}
firstName: {self.firstName}
lastName: {self.lastName}
age: {self.age}
        """)


miku = Student(
    studentId=39,
    firstName="Miku",
    lastName="Hatsune",
    age=16,
)
miku.showInfo()
