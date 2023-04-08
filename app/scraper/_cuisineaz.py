import re

from ._base import ScrapedRecette
from ._helpers import register

__all__ = [
    "RecetteCuisineAZ",
]


class RecetteCuisineAZ(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("h1", {"class": "recipe-title"}).text

    def _get_ingredients(self, soup):
        ingredients = soup.find("section", {"class": "ingredients"}).findAll("li")
        self._ingredients = [ingredient.text.strip() for ingredient in ingredients]

    def _get_directions(self, soup):
        directions = soup.find("section", {"class": "instructions"}).findAll("p")
        self._directions = [direction.text for direction in directions]

    def _get_servings(self, soup):
        servings = soup.find("span", {"id": "LblRecetteNombre"}).text
        self._servings = int(re.sub("[^0-9]", "", servings))


register("www.cuisineaz.com", RecetteCuisineAZ)
