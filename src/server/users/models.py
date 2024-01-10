from pydantic import BaseModel
from typing import List, Optional


class UserInfo(BaseModel):
    id: int
    login: Optional[str] = None
    role_id: int


class ImputUser(BaseModel):
    login: str
    password: int
    role_id: Optional[int] = None


class NewID(BaseModel):
    code: int
    id: int




