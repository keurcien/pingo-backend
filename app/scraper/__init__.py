from ._cuisineactuelle import RecetteCuisineActuelle
from ._cuisineaz import RecetteCuisineAZ
from ._helpers import create_recipe
from ._hervecuisine import RecetteHerveCuisine
from ._jdf import RecetteJournalDesFemmes
from ._madamefigaro import RecetteMadameFigaro
from ._marmiton import RecetteMarmiton
from ._sccg import Recette750g
from .router import router

__all__ = [
    "create_recipe", "router"
]
