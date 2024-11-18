from fastapi_users import schemas
from pydantic import EmailStr
from typing import Optional



class UserRead(schemas.BaseUser[int]):
    username: str
    # class Config:
    #     from_attributes=True


class UserCreate(schemas.BaseUserCreate):
    username: str
    


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]