class India:
    def capital(self) -> None:
        print("New Delhi")

    def language(self) -> None:
        print("Hindi and English")


class USA:
    def capital(self) -> None:
        print("Washington, D.C.")

    def language(self) -> None:
        print("English")


obj_india = India()
obj_usa = USA()
for country in (obj_india, obj_usa):
    country.capital()
    country.language()
