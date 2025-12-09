class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        nick_name: str,
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.nick_name: str = nick_name

    def show_inf(self) -> dict:
        return self.__dict__


user1 = User("John", "Doe", "johnd")
user2 = User("Jane", "Smith", "janes")
user3 = User("Alice", "Johnson", "alicej")
