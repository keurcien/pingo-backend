from fastapi import APIRouter, Depends
from typing import Any
from app.recipes import Recipe, Recipe_Pydantic, RecipeIn_Pydantic
from app.users import User
from app.auth import get_current_user
import datetime
import base64

from google.cloud import storage

def decode_image(data_url):
    format, imgstr = data_url.split(";base64,") 
    ext = format.split("/")[-1] 
    return imgstr, ext

def get_storage_bucket():
    return storage.Client(project="pingo-3dddd").get_bucket("pingo-images")

router = APIRouter(
    prefix="/user/recipes",
    tags=["recipes"],
)

@router.get("/")
async def get_user_recipes(current_user: User = Depends(get_current_user)):
    return await Recipe_Pydantic.from_queryset(Recipe.filter(user=current_user).order_by("-created_at"))

@router.get("/public/{recipe_id}")
async def get_recipe(recipe_id: int):
    return await Recipe.get(id=recipe_id)


@router.delete("/", status_code=204)
async def delete_recipe(
    recipe: RecipeIn_Pydantic, 
    current_user: User = Depends(get_current_user),
    bucket: Any = Depends(get_storage_bucket)
):
    recipe_ = await Recipe.get(id=recipe.id, user=current_user)
    
    if recipe_.image:
        try:
            bucket.blob(recipe_.image).delete()  
        except:
            print("Could not find image on remote storage. Skipping...")
    await recipe_.delete()

@router.post("/")
async def update_recipe(
    recipe: RecipeIn_Pydantic, 
    current_user: User = Depends(get_current_user), 
    bucket: Any = Depends(get_storage_bucket)
):
    print(recipe)
    if recipe.id:
        await Recipe.get(id=recipe.id, user=current_user).update(
            name=recipe.name, 
            ingredients=recipe.ingredients, 
            directions=recipe.directions,
            servings=recipe.servings
        )
        recipe_ = await Recipe.get(id=recipe.id, user=current_user)
    else:
        recipe_ = await Recipe.create(**recipe.dict(exclude={"id", "image"}), user=current_user)

    if recipe.image and ";base64," in recipe.image:
        
        if recipe_.image:
            try:
                bucket.blob(recipe_.image).delete()    
            except:
                print("Could not find image on remote storage. Skipping...")

        image_str, file_extension = decode_image(recipe.image)

        version = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        reference = f"{current_user.username}/{recipe_.id}_{version}.{file_extension}"
        blob = bucket.blob(reference)
        blob.upload_from_string(base64.b64decode(image_str))

        await Recipe.get(id=recipe_.id, user=current_user).update(image=reference)
    
    return await Recipe_Pydantic.from_queryset_single(Recipe.get(id=recipe_.id))
