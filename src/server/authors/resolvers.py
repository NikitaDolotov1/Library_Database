from .models import Author, ImputAuthor, NewID
from typing import List
import sys
sys.path.append('..')
from server.database.db_manager import base_manager


def get_all_authors():
    res = base_manager.execute("SELECT id, FIO FROM authors ", many=True)
    authors = []
    for author in res['data']:
        authors.append(Author(id=author[0], FIO=author[1]))
    return authors


def get_cur_author(author_id: int):
    res = base_manager.execute("SELECT id, FIO FROM authors WHERE id = ?", args=(author_id,), many=True)

    authors = []
    for author in res['data']:
        authors.append(Author(id=author[0], FIO=author[1]))

    return authors

def add_new_author(new_author: ImputAuthor):
    res = base_manager.execute("INSERT INTO authors(FIO)"
                               "VALUES (?)"
                               "RETURNING id ", args=(new_author.FIO,), many=True)
    return NewID(code=res['code'], id=res['data'][0][0])


def delete_author(author_id: int):
    res = base_manager.execute("DELETE FROM authors WHERE id = ?", args=(author_id,))

    return NewID(code=res['code'], id=author_id)
