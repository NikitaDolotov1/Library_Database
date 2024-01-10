from .models import Books, ImputBook, NewID
from typing import List
import sys

sys.path.append('..')
from server.database.db_manager import base_manager


def get_all_books():
    res = base_manager.execute("SELECT id, author, name_book, year_pub,genre FROM books", many=True)
    books = []
    for book in res['data']:
        books.append(Books(id=book[0], author=book[1], name_book=book[2], year_pub=book[3], genre=book[4]))

    return books


def get_book(book_id: int):
    res = base_manager.execute("SELECT id, author, name_book, year_pub, genre FROM books WHERE id = ?",
                                args=(book_id,), many=True)
    books = []
    for book in res['data']:
        books.append(Books(id=book[0], author=book[1], name_book=book[2], year_pub=book[3], genre=book[4]))

    return books


def add_new_book(new_book: ImputBook):
    res = base_manager.execute(
        "INSERT INTO books(author, name_book, year_pub, genre, author_id, genre_id)"
        "VALUES (?, ?, ?, ?, ?, ?)"
        "RETURNING id ",
        args=(new_book.author, new_book.name_book, new_book.year_pub,
              new_book.genre, new_book.author_id, new_book.genre_id,)
        , many=True)

    return NewID(code=res['code'], id=res['data'][0][0])


def delete_book(book_id: int):
    res = base_manager.execute("DELETE FROM books WHERE id = ?", args=(book_id,))

    return NewID(code=res['code'], id=book_id)
