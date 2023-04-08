import re

from ._base import ScrapedRecette
from ._helpers import register

__all__ = ["RecetteMadameFigaro"]


class RecetteMadameFigaro(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("h1", {"class": "mad__titre"}).text

    def _get_servings(self, soup):
        servings = soup.find("div", {"class": "mad__sous-titre"}).find("span").text
        self._servings = int(re.sub("[^0-9]", "", servings))

    def _get_ingredients(self, soup):
        ingredients = soup.find(
            "ul", {"class": "mad__recette__ingredients__info__ingredient__list"}
        ).findAll("li")
        self._ingredients = [ingredient.text.strip() for ingredient in ingredients]

    def _get_directions(self, soup):
        directions = soup.find("div", {"class": "article-body"}).findAll("p")
        self._directions = [direction.text.strip() for direction in directions]


register("madame.lefigaro.fr", RecetteMadameFigaro)
