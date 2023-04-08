import re

import unidecode

from ._base import ScrapedRecette
from ._helpers import register

__all__ = ["RecetteCuisineActuelle"]


class RecetteHerveCuisine(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        name = soup.find("h1", {"class": "post-title"}).text.strip()
        self._name = unidecode.unidecode(name)

    def _get_servings(self, soup):
        servings = soup(text=lambda t: "Portion" in t)[0]
        servings = servings.parent.find_next_sibling()
        servings = servings.text.strip()
        self._servings = int(re.sub("[^0-9]", "", servings))

    def _get_ingredients(self, soup):
        ingredients = soup.find("div", {"class": "recipe-ingredient-list"}).findAll(
            "li"
        )
        self._ingredients = [ingredient.text.strip() for ingredient in ingredients]

    def _get_directions(self, soup):
        directions = soup.find("div", {"class": "recipe-steps"}).findAll("li")
        self._directions = [direction.text.strip() for direction in directions]


register("www.hervecuisine.com", RecetteHerveCuisine)
