
from fastapi import APIRouter
from .models import Roles, ImputRole, NewID
from .resolvers import add_new_role, get_all_roles, get_role, delete_roles
from typing import List

router = APIRouter()

@router.get('/', tags=["roles"])
def get_roles() -> List[Roles]:
    return get_all_roles()


@router.get("/{role_id}", tags=["roles"])
def get_current_role(role_id: int) -> List[Roles]:
    return get_role(role_id)

@router.post('/', tags=["roles"])
def add_role(new_role: ImputRole) -> NewID:
    return add_new_role(new_role)

@router.delete("/{role_id}", tags=["roles"])
def delete_cur_user(role_id: int) -> NewID:
    return delete_roles(role_id)
