
from fastapi import APIRouter
from .models import Books, ImputBook, NewID
from .resolvers import get_all_books, get_book, add_new_book, delete_book
from typing import List

router = APIRouter()

@router.get('/', tags=["books"])
def get_books() -> List[Books]:
    return get_all_books()

@router.post('/', tags=["books"])
def add_book(new_book: ImputBook) -> NewID:
    return add_new_book(new_book)


@router.get("/{book_id}", tags=["books"])
def get_current_book(book_id: int) -> List[Books]:
    return get_book(book_id)


@router.delete("/{book_id}", tags=["books"])
def delete_cur_book(book_id: int) -> NewID:
    return delete_book(book_id)

