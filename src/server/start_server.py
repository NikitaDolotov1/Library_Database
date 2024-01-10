import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.db_manager import base_manager
from users.routers import router as user_router
from genres.routers import router as genre_router
from roles.routers import router as role_router
from authors.routers import router as author_router
from books.routers import router as books_router
from books_out.routers import router as books_out_router
from settings import SCRIPTS_PRIMARY_DATA_PATH, SCRIPTS_TABLES_PATH

app = FastAPI()

app.include_router(user_router, prefix='/users')
app.include_router(genre_router, prefix='/genres')
app.include_router(role_router, prefix='/roles')
app.include_router(author_router, prefix='/authors')
app.include_router(books_router, prefix='/books')
app.include_router(books_out_router, prefix='/books_out')


@app.get('/')
def root():
    return RedirectResponse("/docs")


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_PRIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)
