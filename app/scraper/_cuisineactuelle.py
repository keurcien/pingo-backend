from ._base import ScrapedRecette
from ._helpers import register

__all__ = ["RecetteCuisineActuelle"]


class RecetteCuisineActuelle(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("h1", {"class": "recipe-title"}).text

    def _get_servings(self, soup):
        self._servings = int(
            soup.find("input", {"class": "recipeIngredients-yieldInput"}).attrs["value"]
        )

    def _get_ingredients(self, soup):
        ingredients = soup.findAll("li", {"class": "recipeIngredients-ingredient"})
        self._ingredients = [ingredient.text.strip() for ingredient in ingredients]

    def _get_directions(self, soup):
        directions = soup.find("div", {"class": "recipe-instructionContent"}).findAll(
            "li"
        )
        self._directions = [direction.text.strip() for direction in directions]


register("www.cuisineactuelle.fr", RecetteCuisineActuelle)
