from fastapi import APIRouter
from .models import ImputUser, UserInfo, NewID
from .resolvers import get_all_users, get_user, add_new_user, delete_user, update_user, check_user
from typing import List

router = APIRouter()


@router.get('/check', tags=["users"])
def check_exists_user(user: ImputUser) -> UserInfo:
    return check_user(user)


@router.get('/', tags=["users"])
def get_users() -> List[UserInfo]:
    return get_all_users()


@router.post('/', tags=["users"])
def add_user(new_user: ImputUser) -> NewID:
    return add_new_user(new_user)


@router.get("/{user_id}", tags=["users"])
def get_current_user(user_id: int) -> List[UserInfo]:
    return get_user(user_id)


@router.delete("/{user_id}", tags=["users"])
def delete_cur_user(user_id: int) -> NewID:
    return delete_user(user_id)


@router.put("/{user_id}", tags=["users"])
def update_cur_user(user_id: int, new_user_name: ImputUser) -> NewID:
    return update_user(user_id, new_user_name)

