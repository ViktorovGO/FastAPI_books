from hmac import new
from os import name
from re import A
import re
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from auth.models import User
from auth.router import current_user

from database import get_async_session

from .models import Book
from books.scemas import BooksCreate


router = APIRouter(
    prefix = '/books',
    tags = ["Books"]
)


@router.get('/')
async def get_all_books(session: AsyncSession = Depends(get_async_session)):
    query = select(Book)
    books = await session.execute(query)
    return books.mappings().all()

@router.post("/")
async def add_book(new_book: BooksCreate, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    new_book = new_book.dict()
    new_book['book_owner'] = user.id
    stat = insert(Book).values(**new_book)
    await session.execute(stat)
    await session.commit()
    return {"status":"success"}