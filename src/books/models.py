from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from auth.models import User

Base = declarative_base()
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key = True)
    book_title = Column(String)
    book_owner = Column(Integer, ForeignKey(User.id))
