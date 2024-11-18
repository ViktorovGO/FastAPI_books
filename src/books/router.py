from hmac import new
from lib2to3.pgen2.token import AT
from os import name
from re import A
import re
from turtle import st, update
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Update, select, insert

from auth.models import User
from auth.router import current_user

from database import get_async_session

from .models import Book
from books.scemas import BookCreate, BookEdit


router = APIRouter(
    prefix = '/books',
    tags = ["Books"]
)


@router.get('/')
async def get_all_books(session: AsyncSession = Depends(get_async_session)):
    query = select(Book)
    books = await session.execute(query)
    return books.mappings().all()

@router.get('/mybooks')
async def get_my_books(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    query = select(Book).where(Book.book_owner == user.id)
    books = await session.execute(query)
    return books.mappings().all()

@router.post("/")
async def add_book(new_book: BookCreate, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    new_book = new_book.dict()
    new_book['book_owner'] = user.id
    stat = insert(Book).values(**new_book)
    await session.execute(stat)
    await session.commit()
    return {"status":"success"}

@router.patch('/{book_id}')
async def edit_book(edit_book: BookEdit, book_id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    try:
        curr_book = await session.get(Book, book_id)
        stmt = Update(Book).where(Book.id == book_id).values(**edit_book.dict())
        if user.id == curr_book.book_owner or user.is_superuser == True:
            await session.execute(stmt)
        else:
            raise HTTPException(status_code=503, detail="Forbidden")
        await session.commit()

        return curr_book
    
    except AttributeError:
        raise HTTPException(status_code=404, detail="Book not found")
    
    