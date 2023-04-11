from fastapi import APIRouter, Response
from pydantic import BaseModel
from typing import List
from . import calculator

class Ingredients(BaseModel):
    ingredients: List[str]

router = APIRouter(
    prefix="/calories"
)

@router.post("/")
def calculate_calories(ingredients: Ingredients, resp: Response):
    calc = calculator.Calculator(calculator.NUTRIENT_DB)

    calories = calc.calculate(ingredients.ingredients)
    resp.status_code = 200

    return calories
