
from fastapi import APIRouter
from .models import Genres, ImputGenre, NewID
from .resolvers import get_all_genres, add_new_genre, get_genre, delete_genre
from typing import List

router = APIRouter()


@router.get('/', tags=["genres"])
def get_genres() -> List[Genres]:
    return get_all_genres()

@router.get("/{genre_id}", tags=["genres"])
def get_current_user(genre_id: int) -> List[Genres]:
    return get_genre(genre_id)

@router.post('/', tags=["genres"])
def add_genres(new_genre: ImputGenre) -> NewID:
    return add_new_genre(new_genre)


@router.delete("/{genre_id}", tags=["genres"])
def delete_cur_genre(genre_id: int) -> NewID:
    return delete_genre(genre_id)
