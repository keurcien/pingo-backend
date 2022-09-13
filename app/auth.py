import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.users import User

cred = credentials.Certificate("pingo-3dddd-firebase-adminsdk-5s59l-7f67358774.json")
firebase_admin.initialize_app(cred)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def decode_token(id_token: str) -> dict:
    decoded_token = auth.verify_id_token(id_token)
    return decoded_token["uid"], decoded_token["email"]

async def get_current_user(token: str = Depends(oauth2_scheme)):
    uid, email = decode_token(token)
    user, _ = await User.get_or_create(username=uid, email=email)
    return user