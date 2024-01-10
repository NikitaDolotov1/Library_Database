from pydantic import BaseModel
from typing import List, Optional


class Books(BaseModel):
    id: int
    author: str
    name_book: str
    year_pub: int
    genre: str


class ImputBook(BaseModel):
    author: str
    name_book: str
    year_pub: int
    genre: str
    author_id: int
    genre_id: int



class NewID(BaseModel):
    code: int
    id: int




