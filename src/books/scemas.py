from pydantic import BaseModel


class BooksCreate(BaseModel):
    book_title: str
    