from unicodedata import normalize

from ._base import ScrapedRecette
from ._helpers import register

__all__ = ["RecetteMarmiton"]


class RecetteMarmiton(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self.soup = soup
        self._name = soup.find("h1", {"class": "itJBWW"}).text

    def _get_servings(self, soup):
        servings = soup.find("span", {"class": "knYsyq"}).text
        self._servings = int(servings)

    def _get_ingredients(self, soup):
        self._ingredients = []
        ingredients = soup.findAll("div", {"class": "MuiGrid-item"})

        for ingredient in ingredients:
            quantity = ingredient.find("span", {"class": "epviYI"})
            quantity = quantity.text.strip() if quantity else quantity
            name = ingredient.find("span", {"class": "kWuxfa"})
            name = name.text.strip() if name else name

            self._ingredients.append(normalize("NFKD", f"{quantity} {name}".strip()))

    def _get_directions(self, soup):
        directions = soup.findAll("p", {"class": "bFBrMO"})
        self._directions = [direction.text.strip() for direction in directions]


register("www.marmiton.org", RecetteMarmiton)
