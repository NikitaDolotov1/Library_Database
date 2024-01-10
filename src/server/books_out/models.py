from pydantic import BaseModel
from typing import List, Optional


class Books_outInfo(BaseModel):
    id: int
    id_book: int
    date_out: str
    date_in: str



class ImputBook_out(BaseModel):
    id_book: int
    date_out: str
    date_in: str


class NewID(BaseModel):
    code: int
    id: int




