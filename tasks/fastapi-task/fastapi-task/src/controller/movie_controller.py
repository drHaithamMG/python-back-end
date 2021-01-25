from fastapi import HTTPException
from pydantic import UUID4
from fastapi import APIRouter
from src.models.pydantic.movies import Movie, MovieOut, CustomeMessages
from src.models.movies import MoviesSQL
movies_router = APIRouter()

@movies_router.get('/api/movies', tags=["movies"])
async def get_all():
    """Get all movies from the database"""
    return MoviesSQL


@movies_router.get('/api/movies/{movie_uuid}', tags=["movies"])
async def get_movie(movie_uuid: UUID4):
    """Get a specific movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass


@movies_router.post('/api/movies/', response_model=MovieOut, tags=["movies"])
async def add_movie(movie: Movie):
    """Add a new movie"""
    pass


@movies_router.delete('/api/movies/{movie_uuid}', response_model=CustomeMessages, tags=["movies"])
async def remove_movie(movie_uuid: UUID4):
    """Remove a movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')

    # return CustomeMessages('Movie has been successfully deleted')
    pass


@movies_router.patch('/api/movies/{movie_uuid}', response_model=MovieOut, tags=["movies"])
async def edit_movie(movie_uuid: UUID4):
    """Edit movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass
