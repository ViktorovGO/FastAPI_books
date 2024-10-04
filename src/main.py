from fastapi_users import FastAPIUsers
from auth.models import User
from auth.scemas import UserCreate, UserRead, UserUpdate
from auth.service import auth_backend
from fastapi import Depends, FastAPI

from auth.utils import get_user_manager


app = FastAPI(
    title='Библиотека'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"

@app.get("/books", tags=['Books'])
async def get_books(pwd: str):

    return {'status':'success'}