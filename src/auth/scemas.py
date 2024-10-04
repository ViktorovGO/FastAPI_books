from fastapi_users import schemas
from pydantic import EmailStr
from typing import Optional

class UserRead(schemas.BaseUser[int]):
    email:str
    # password: str

class UserCreate(schemas.BaseUserCreate):
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass
