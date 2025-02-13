from ..schemas.user_schema import UserCreate
from ..services.user_service import get_by_email, get_by_username, create
from ..services.jwt_service  import create_access_token
from ..schemas.user_schema import UserSchema
from fastapi import HTTPException, status
from ..utils.bcrypt_hashing import get_hashed_password, verify_password
from ..models.models import User
from datetime import datetime, timedelta, timezone
import os

access_token_expire_minutes = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))



def authenticate_user(username:str, password:str) -> bool | User:
  result  = get_by_username(username)
  
  #raise exception if username not present 
  if not result:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail=f'Incorrect sign in credentials')
  user = result[0]
  if not verify_password(password, user.password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail=f'Incorrect sign in credentials')
    
  return user 


def register(user: UserCreate) -> UserSchema:
  """
  returns newly created user
  """
  user_exists_by_email = get_by_email(user.email)
  user_exists_by_username = get_by_username(user.username)

  #hash incoming password
  user.password = get_hashed_password(user.password)

  if user_exists_by_email:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="a user with this email already exists")

  if user_exists_by_username:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="a user with this username already exists")

  return create(user)

def login(username: str, password: str):
  """
  returns login data 
  """
  #authenticate user 
  user = authenticate_user(username, password)

  if not user:
     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail=f'there is no user with this username or password')
  
  #create JWT token 
  access_token_expires = timedelta(minutes=access_token_expire_minutes)
  token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
  
  #return the token
  return {"access_token": token, "token_type": "bearer", "username": username}
  
   