__all__ = [
    "create_recipe",
]

recettes_map = {}


def create_recipe(url):
    tokens = url.split("/")
    for base_url, recette in recettes_map.items():
        
        if base_url in tokens:
            return recette(url)


def register(base_url, recette):
    recettes_map[base_url] = recette
