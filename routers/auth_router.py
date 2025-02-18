from fastapi import Depends, APIRouter, Response
from ..schemas.user_schema import UserCreate
from ..controllers import auth_controller
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..schemas.token_schema import TokenData
import os

cookies_key_name= os.getenv("COOKIES_KEY_NAME")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(signupdata: UserCreate):
    registered_user = auth_controller.register(signupdata)
    return(registered_user)

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], res: Response) -> TokenData:
    jwt_token = auth_controller.login(form_data.username, form_data.password)
    res.set_cookie(cookies_key_name, jwt_token["access_token"])
    return jwt_token
    
