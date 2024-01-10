
from fastapi import APIRouter
from .models import Books_outInfo, ImputBook_out, NewID
from .resolvers import get_all_books_out, get_book_out, add_new_book_out, delete_book_out
from typing import List

router = APIRouter()

@router.get('/', tags=["books_out"])
def get_books_out() -> List[Books_outInfo]:
    return get_all_books_out()

@router.get("/{book_out_id}", tags=["books_out"])
def get_current_book(book_out_id: int) -> List[Books_outInfo]:
    return get_book_out(book_out_id)


@router.post('/', tags=["books_out"])
def add_book_out(new_book_out: ImputBook_out) -> NewID:
    return add_new_book_out(new_book_out)


@router.delete("/{book_out_id}", tags=["books_out"])
def delete_cur_book(book_out_id: int) -> NewID:
    return delete_book_out(book_out_id)
