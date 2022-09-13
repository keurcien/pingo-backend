from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from .recipes import router as recipes_router
from . import DB_CONFIG

app = FastAPI()
app.include_router(recipes_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    config={
        'connections': {
            # Dict format for connection
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': DB_CONFIG
            },
        },
        'apps': {
            'models': {
                'models': ['app.recipes.models', 'app.users.models'],
                # If no default_connection specified, defaults to 'default'
                'default_connection': 'default',
            }
        }
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

