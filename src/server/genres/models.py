from pydantic import BaseModel
from typing import List, Optional


class Genres(BaseModel):
    id: int
    name_genre: str


class ImputGenre(BaseModel):
    name_genre: str


class NewID(BaseModel):
    code: int
    id: int
