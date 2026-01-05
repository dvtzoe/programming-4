import os

import openai
from dotenv import load_dotenv

load_dotenv()


class OpenaiClient:
    def __init__(self) -> None:
        base_url = os.getenv("OPENAI_BASE_URL")
        api_key = os.getenv("OPENAI_API_KEY")
        self.openai: openai.OpenAI = openai.OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

    def create_chat_completion(
        self,
        prompt: str,
        model: str = "openai/gpt-5",
    ) -> str:
        response = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content or "idk"


openai_client = OpenaiClient()


class Animal:
    classOfLivingThings: str = "Animal Kingdom"  # noqa: N815

    def __init__(
        self,
        habitat: str | None,
        weight: float | None,
        species: str,
    ) -> None:
        self.habitat: str = habitat or "lagoon"
        self.weight: float = weight or 0.0
        self.species: str = species

    def getClassOfLivingThings(self) -> str:  # noqa: N802
        return self.classOfLivingThings

    def getHabitat(self) -> str:  # noqa: N802
        return self.habitat

    def getSpecie(self) -> str:  # noqa: N802
        return self.species

    def getWeight(self) -> float:  # noqa: N802
        return self.weight

    def setSpecie(  # noqa: N802
        self,
        speciesName: str,  # noqa: N803
    ) -> str:
        self.species = speciesName
        return self.getSpecie()

    def setWeight(  # noqa: N802
        self,
        grams: float = 0.1,
    ) -> float:
        self.weight = grams
        return self.getWeight()


class Egg:
    def __init__(
        self,
        colour: str = "white",
    ) -> None:
        self.colour: str = colour

    def getIncubationPeriod(self) -> int:  # noqa: N802
        return int(
            openai_client.create_chat_completion(
                "give me an egg incubation period with ONLY 1 number and nothing else"
            )
        )


class Venom:
    def __init__(
        self,
        concentrationLevel: str = "low",  # noqa: N803
    ) -> None:
        self.concentrationLevel: str = concentrationLevel

    def setConcentrationLevel(  # noqa: N802
        self,
        _level: str,
    ) -> str:
        self.concentrationLevel = _level
        return self.getConcentrationLevel()

    def getConcentrationLevel(self) -> str:  # noqa: N802
        return self.concentrationLevel


class Platypus(Animal):
    def __init__(
        self,
        legs: int = 4,
        tail: int = 1,
    ) -> None:
        self.egg = Egg()
        self.venom = Venom()

        self.legs: int = legs
        self.tail: int = tail

    def dive(self) -> bool:
        return (
            "yes" in openai_client.create_chat_completion("Can platypuses fly.").lower()
        )

    def parentalCare(self) -> str:  # noqa: N802
        return openai_client.create_chat_completion(
            "How do platypuses do parental care"
        )


class Aves(Animal):
    def __init__(
        self,
        wings: int = 2,
    ) -> None:
        self.wings: int = wings

    def eggLaying(self) -> None:  # noqa: N802
        return

    def canFly(self) -> bool:  # noqa: N802
        return "yes" in openai_client.create_chat_completion("Can aveses fly.").lower()


class Cockoo(Aves):
    def __init__(
        self,
        legs: int = 2,
        tail: int = 1,
    ) -> None:
        self.legs: int = legs
        self.tail: int = tail

    def fly(self) -> bool:
        return "yes" in openai_client.create_chat_completion("Can cuckoos fly.").lower()

    def parentalCare(self) -> str:  # noqa: N802
        return openai_client.create_chat_completion("How do cuckoos do parental care")
