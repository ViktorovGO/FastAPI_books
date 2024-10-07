import uvicorn


from fastapi import Depends, FastAPI

from auth.models import User
from auth.scemas import UserCreate, UserRead, UserUpdate
from auth.service import auth_backend
from auth.router import fastapi_users, current_user

from books.router import router as books_router


app = FastAPI(
    title='Библиотека'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
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
    tags=["Users"],
)

app.include_router(books_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
