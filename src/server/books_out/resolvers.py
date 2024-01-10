from .models import Books_outInfo, ImputBook_out, NewID
from typing import List
import sys

sys.path.append('..')
from server.database.db_manager import base_manager

def get_all_books_out():
    res = base_manager.execute("SELECT id, id_book, date_out, date_in FROM books_out", many=True)
    books = []
    for book in res['data']:
        books.append(Books_outInfo(id=book[0], id_book=book[1], date_out=book[2], date_in=book[3]))

    return books
def get_book_out(book_out_id: int):
    res = base_manager.execute("SELECT id, id_book, date_out, date_in FROM books_out WHERE id = ?",
                                args=(book_out_id,), many=True)
    books = []
    for book in res['data']:
        books.append(Books_outInfo(id=book[0], id_book=book[1], date_out=book[2], date_in=book[3]))

    return books

def add_new_book_out(new_book_out: ImputBook_out):
    res = base_manager.execute(
        "INSERT INTO books_out(id_book, date_out, date_in)"
        "VALUES (?, ?, ?)"
        "RETURNING id",
        args=(new_book_out.id_book, new_book_out.date_out, new_book_out.date_in)
        , many=True)

    return NewID(code=res['code'], id=res['data'][0][0])


def delete_book_out(book_out_id: int):
    res = base_manager.execute("DELETE FROM books_out WHERE id = ?", args=(book_out_id,))

    return NewID(code=res['code'], id=book_out_id)
