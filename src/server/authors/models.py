from pydantic import BaseModel
from typing import List, Optional


class Author(BaseModel):
    id: int
    FIO: str


class ImputAuthor(BaseModel):
    FIO: str


class NewID(BaseModel):
    code: int
    id: int
