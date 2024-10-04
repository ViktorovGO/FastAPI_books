from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import Column, Integer

Base: DeclarativeMeta = declarative_base()
class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
