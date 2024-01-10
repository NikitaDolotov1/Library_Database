from .models import Genres,ImputGenre,NewID
from typing import List
import sys
sys.path.append('..')
from server.database.db_manager import base_manager


def get_all_genres():
    res = base_manager.execute("SELECT id, name_genre FROM genres ", many=True)
    genres = []
    for genre in res['data']:
        genres.append(Genres(id=genre[0], name_genre=genre[1]))
    return genres


def get_genre(genre_id: int):
    res = base_manager.execute("SELECT id, name_genre FROM genres WHERE id = ?", args=(genre_id,), many=True)

    genres = []
    for genre in res['data']:
        genres.append(Genres(id=genre[0], name_genre=genre[1]))

    return genres


def add_new_genre(new_genre: ImputGenre):
    res = base_manager.execute("INSERT INTO genres(name_genre)"
                               "VALUES (?)"
                               "RETURNING id ", args=(new_genre.name_genre,), many=True)
    return NewID(code=res['code'], id=res['data'][0][0])


def delete_genre(genre_id: int):
    res = base_manager.execute("DELETE FROM genres WHERE id = ?", args=(genre_id,))

    return NewID(code=res['code'], id=genre_id)
