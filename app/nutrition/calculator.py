import unidecode
from lunr import lunr

from .converter import Converter
from .db import NUTRIENT_DB
from .normalizer import Normalizer
from .parser import Parser

DEFAULT_VALUE = {"calories": 0, "proteines": 0, "glucides": 0, "lipides": 0, "from": ""}

UNIT_TYPE = {
    "ml": "volume",
    "cl": "volume",
    "dl": "volume",
    "l": "volume",
    "g": "weight",
    "kg": "weight",
}


def normalize(ingredient):
    ingredient_ = ingredient.lower()
    ingredient_ = unidecode.unidecode(ingredient_)
    ingredient_ = ingredient_.replace(" de ", " ").replace(" d'", " ")
    return ingredient_


def create_index(nutrient_db):
    return [
        {
            "id": str(id_),
            "name": normalize(nutrient["name"]),
            "unit": nutrient["unit"],
            "calories": nutrient.get("calories", 0),
            "proteines": nutrient.get("proteines", 0),
            "glucides": nutrient.get("glucides", 0),
            "lipides": nutrient.get("lipides", 0),
        }
        for id_, nutrient in enumerate(nutrient_db)
    ]


class Calculator:
    def __init__(self, nutrient_db=None):
        nutrient_db = nutrient_db if nutrient_db else NUTRIENT_DB
        self.nutrient_db = create_index(nutrient_db)
        self.engine = lunr(ref="id", fields=("name",), documents=self.nutrient_db)
        self.converter = Converter()
        self.normalizer = Normalizer()
        self.parser = Parser()

        # Map nutrients to accelerate search
        # Note that currently, it looks like {'i': i} but that implementation should allow for other type of IDs
        self._nutrient_map = {
            nutrient["id"]: i for i, nutrient in enumerate(self.nutrient_db)
        }

    def find_nutrient(self, document, unit):
        idx = self._nutrient_map.get(document)
        if idx is not None:
            nutrient = self.nutrient_db[idx]
            cond = (
                unit == nutrient["unit"]
                if unit not in UNIT_TYPE
                else UNIT_TYPE.get(unit) == UNIT_TYPE.get(nutrient["unit"])
            )
            if cond:
                # print(f"{document}:{unit} Found nutrient {nutrient}\n")
                return nutrient

    def fully_match(self, metadata, document):
        matching_patterns = list(metadata.keys())
        return len(matching_patterns) == len(
            self.normalizer.normalize(document["name"]).split()
        )

    def filter_(self, search_results, unit):
        for search_result in search_results:
            document = self.find_nutrient(search_result["ref"], unit)
            metadata = search_result["match_data"].metadata
            if document and self.fully_match(metadata, document):
                return document

    def _calculate(self, ingredient):
        ingredient_ = self.normalizer.normalize(ingredient)
        search_result = self.engine.search(ingredient_)

        if search_result:
            value, unit = self.parser.parse(ingredient_)
            value, unit = self.converter.convert(value, unit)
            nutrient = self.filter_(search_result, unit)

            if value and nutrient:
                fac = float(value)
                fac *= self.converter.convert(1.0, nutrient["unit"])[0]

                calories = nutrient["calories"] * fac
                proteines = nutrient["proteines"] * fac
                glucides = nutrient["glucides"] * fac
                lipides = nutrient["lipides"] * fac

                return {
                    "calories": calories,
                    "proteines": proteines,
                    "glucides": glucides,
                    "lipides": lipides,
                    "from": nutrient["name"],
                }
            else:
                return DEFAULT_VALUE
        else:
            # print(f"{ingredient} not found")
            return DEFAULT_VALUE

    def calculate(self, ingredients):
        return [
            {"ingredient": ingredient, **self._calculate(ingredient)}
            for ingredient in ingredients
        ]
