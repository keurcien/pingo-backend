import re

from ._base import ScrapedRecette
from ._helpers import register

__all__ = [
    "RecetteJournalDesFemmes",
]


class RecetteJournalDesFemmes(ScrapedRecette):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("h1", {"class": "app_recipe_title_page"}).text

    def _get_ingredients(self, soup):
        self._ingredients = []

        if soup.find("ul", {"class": "bu_cuisine_ingredients"}):
            ingredients = soup.find("ul", {"class": "bu_cuisine_ingredients"}).findAll(
                "li"
            )

            for ingredient in ingredients:
                ingredient_ = ingredient.find(
                    "a", {"class": "bu_cuisine_pointille_vert name"}
                )

                if ingredient_:
                    name = ingredient_.text.strip()
                    quantity = ingredient_.previous_sibling
                    if quantity:
                        quantity = quantity.strip()
                        self._ingredients.append(f"{quantity} {name}")
                    else:
                        self._ingredients.append(name)
        else:
            recipe_list = soup.find("ul", {"class": "app_recipe_list"})
            ingredients = recipe_list.findAll("h3", {"class": "app_recipe_ing_title"})
            if not ingredients:
                ingredients = soup.findAll("h4", {"class": "app_recipe_ing_title"})

            for ingredient in ingredients:
                name = (
                    ingredient.a.text.strip()
                    if ingredient.a
                    else ingredient.text.strip().split("\n")[0]
                )

                if ingredient.span:
                    quantity = ingredient.span.text.replace("\n", "")
                    quantity = " ".join(quantity.split())
                    if quantity:
                        self.ingredients.append(f"{quantity} {name}")
                    else:
                        self.ingredients.append(name)
                else:
                    self.ingredients.append(name)

    def _get_directions(self, soup):
        self._directions = []

        directions = soup.findAll("li", {"class": "bu_cuisine_recette_prepa"})
        for direction in directions:
            direction_ = direction.text.replace("\n", "")
            tokens = direction_.split()
            if tokens[0] == "Pour":
                direction_ = " ".join(tokens[2:])
            else:
                direction_ = " ".join(tokens[1:])
            self._directions.append(direction_)

    def _get_servings(self, soup):
        if soup.find("span", {"id": "numberPerson"}):
            servings = soup.find("span", {"id": "numberPerson"}).text
        else:
            servings = soup.find("span", {"class": "bu_cuisine_title_3--subtitle"}).text

        self._servings = int(re.sub("[^0-9]", "", servings))


register("cuisine.journaldesfemmes.fr", RecetteJournalDesFemmes)
