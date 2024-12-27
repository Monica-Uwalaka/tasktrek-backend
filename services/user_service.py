from ..database import session_maker
from ..models.models import User as UserModel
from ..schemas.user_schema import UserCreate, UserSchema
from sqlalchemy import select

def get_by_id(user_id: int) -> UserModel:
    """ 
    returns the first row from the executed query to find a user by id 
    """
    session = session_maker()
    return session.execute(select(UserModel).where(UserModel.id==id)).first()

def get_by_email(email: str) -> UserModel:
    """ 
    returns the first row from the executed query to find a user by email
    """
    session = session_maker()
    return session.execute(select(UserModel).where(UserModel.email==email)).first()

def get_by_username(username: str):
    """ 
    returns the first row from the executed query to find a user by username
    """
    session = session_maker()
    return session.execute(select(UserModel).where(UserModel.username==username)).first()

def create(user_data: UserCreate) -> UserSchema:
    new_user = UserModel()
    new_user.username = user_data.username
    new_user.firstname = user_data.firstname
    new_user.lastname = user_data.lastname
    new_user.email = user_data.email
    new_user.password = user_data.password

    session = session_maker()
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return UserSchema(id=new_user.id, firstname=new_user.firstname, lastname=new_user.lastname, 
                       email=new_user.email,username=new_user.username, 
                       is_active=new_user.is_active)

def update():
    pass

def delete():
    pass