from pydantic import BaseModel
from typing import List, Optional


class Roles(BaseModel):
    id: int
    role_name: str

class ImputRole(BaseModel):
    role_name: str

class NewID(BaseModel):
    code: int
    id: int
