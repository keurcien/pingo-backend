import requests
from abc import abstractmethod, ABC
from bs4 import BeautifulSoup


__all__ = [
    "ScrapedRecette",
]


class Recette(ABC):
    def __init__(self, name=None, servings=None, ingredients=None, directions=None):
        self._name = name if name else ""
        self._servings = servings if servings else 1
        self._ingredients = ingredients if ingredients else []
        self._directions = directions if directions else []

    def __repr__(self):
        out = [f"{self.name.capitalize()}"]
        out += [f"{'=' * len(out[-1])}\n"]

        out += [f"Ingredients ({self.servings} servings)"]
        out += [f"{'-' * len(out[-1])}"]
        out += self.ingredients
        out[-1] = f"{out[-1]}\n"

        out += ["Directions"]
        out += [f"{'-' * len(out[-1])}"]
        out += [
            f"{i + 1}. {direction.capitalize()}"
            for i, direction in enumerate(self.directions)
        ]

        return "\n".join(out)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def servings(self):
        return self._servings

    @servings.setter
    def servings(self, value):
        self._servings = value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

    @property
    def directions(self):
        return self._directions

    @directions.setter
    def directions(self, value):
        self._directions = value


class ScrapedRecette(Recette):
    def __init__(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        self._url = url
        self._get_name(soup)
        self._get_servings(soup)
        self._get_ingredients(soup)
        self._get_directions(soup)

    @abstractmethod
    def _get_name(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_servings(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_ingredients(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_directions(self, soup):
        raise NotImplementedError()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
