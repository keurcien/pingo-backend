import re

import unidecode


class Normalizer:
    def __init__(self):
        self.table = {
            "cac": ["c a c", "cuillere a cafe", "cuilleres a cafe"],
            "cas": ["c a s", "cuillere a soupe", "cuilleres a soupe"],
        }

        self.teaspoon_pattern, self.teaspoon_variants = self.build_pattern("cac")
        self.tablespoon_pattern, self.tablespoon_variants = self.build_pattern("cas")

    def build_pattern(self, substitute):
        variants_ = self.table.get(substitute)
        variants_ = dict((re.escape(variant), substitute) for variant in variants_)
        return re.compile("|".join(variants_.keys())), variants_

    def teaspoon(self, ingredient):
        return self.teaspoon_pattern.sub(
            lambda m: self.teaspoon_variants[re.escape(m.group(0))], ingredient
        )

    def tablespoon(self, ingredient):
        return self.tablespoon_pattern.sub(
            lambda m: self.tablespoon_variants[re.escape(m.group(0))], ingredient
        )

    def remove_stopwords(self, ingredient):
        ingredient_ = ingredient.replace(" de ", " ")
        ingredient_ = ingredient_.replace(" d'", " ")
        return ingredient_

    def remove_additional_info(self, ingredient):
        ingredient_ = re.sub("[\(\[].*?[\)\]]", "", ingredient)
        ingredient_ = re.sub("[^0-9a-zA-Z.,/ ]+", "", ingredient_)
        return ingredient_

    def stem(self, ingredient):
        tokens = ingredient.split(" ")

        def remove_x(word):
            if word.endswith("eaux"):
                return word.replace("eaux", "eau")
            else:
                return word

        return " ".join([remove_x(word) for word in tokens])

    def normalize(self, ingredient):
        ingredient_ = ingredient.lower()
        ingredient_ = unidecode.unidecode(ingredient_)
        ingredient_ = self.remove_stopwords(ingredient_)
        ingredient_ = self.remove_additional_info(ingredient_)
        ingredient_ = self.teaspoon(ingredient_)
        ingredient_ = self.tablespoon(ingredient_)
        ingredient_ = self.stem(ingredient_)
        return ingredient_.strip()
