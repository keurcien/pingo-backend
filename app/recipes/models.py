from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
from typing import Optional, List

class Recipe(Model):
    id = fields.IntField(pk=True, generated=True)
    user = fields.relational.ForeignKeyField("models.User", on_delete=fields.CASCADE)
    name = fields.CharField(max_length=300)
    ingredients = fields.JSONField()
    directions = fields.JSONField()
    servings = fields.IntField(default=1)
    url = fields.TextField(null=True)
    image = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "recipes"

class RecipeIn_Pydantic(BaseModel):
    id: Optional[int]
    name: str
    ingredients: List[str]
    directions: List[str]
    servings: int
    url: Optional[str]
    image: Optional[str]

Recipe_Pydantic = pydantic_model_creator(Recipe, name="Recipe")