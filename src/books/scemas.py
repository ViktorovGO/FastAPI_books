from token import OP
from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    book_title: str
    
class BookEdit(BaseModel):
    book_title: Optional[str]
    