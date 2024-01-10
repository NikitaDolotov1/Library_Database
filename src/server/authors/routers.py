from fastapi import APIRouter
from .models import Author, ImputAuthor, NewID
from .resolvers import get_all_authors, add_new_author, get_cur_author, delete_author
from typing import List

router = APIRouter()


@router.get('/', tags=["authors"])
def get_author() -> List[Author]:
    return get_all_authors()

@router.get("/{author_id}", tags=["authors"])
def get_current_author(author_id: int) -> List[Author]:
    return get_cur_author(author_id)


@router.post('/', tags=["authors"])
def add_author(new_author: ImputAuthor) -> NewID:
    return add_new_author(new_author)


@router.delete("/{author_id}", tags=["authors"])
def delete_cur_author(author_id: int) -> NewID:
    return delete_author(author_id)
