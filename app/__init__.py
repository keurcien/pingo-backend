import os
from dotenv import load_dotenv

load_dotenv(".env")

DB_CONFIG = {
    "host": os.getenv("PG_HOST"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "database": os.getenv("PG_DATABASE"),
    "port": os.getenv("PG_PORT")
}

__all__ = [DB_CONFIG]