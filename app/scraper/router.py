from fastapi import APIRouter, Response
from pydantic import BaseModel
import logging
from . import create_recipe

logger = logging.getLogger(__name__)

class RecetteURL(BaseModel):
    url: str

router = APIRouter(
    prefix="/scraper"
)

@router.post("/")
def fetch_recette(url: RecetteURL, resp: Response):
    url = url.url

    try:
        r = create_recipe(url)

        if not r.ingredients:
            logger.error(f"Couldn't retrieve ingredients: {url}")

            if not r.directions:
                logger.error(f"Couldn't retrieve directions: {url}")

            if len(r.ingredients) == 1:
                logger.warning(f"Found only one ingredient: {url}")

            if len(r.directions) == 1:
                logger.warning(f"Found only one direction: {url}")

        resp.status_code = 200

        return {
            "url": r.url,
            "name": r.name,
            "ingredients": r.ingredients,
            "directions": r.directions,
            "servings": r.servings,
        }

    except Exception as e:
        logger.error(e)
        logger.error(f"Scraping failed: {url}")

        resp.status_code = 400


