from pydantic import BaseModel, EmailStr

"""
    schema is AKA pydantic model
    ClassBase schema: defines the common attributes for creating and reading data for each model
    ClassCreate schema: inherits from the base class and provides additional attributes needed at creation
    class schema: inherits from the base class and provides additional attributes needed when reading data and returning it from the API
"""

#user schema
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    username:  str

class UserCreate(UserBase):
    email: str
    password: str

class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserSchema(UserBase):
    id: int
    is_active: bool
    # tasks: list[Task] = []
    # goal: Goal

    class Config:
        orm_mode = True