from fastapi import HTTPException
from pydantic import UUID4
from fastapi import APIRouter
from src.models.pydantic.movies import CustomeMessages
from src.models.pydantic.movie_details import MovieDetails, MovieDetailsOut
movie_details_router = APIRouter()


@movie_details_router.get('/api/details_list', response_model=MovieDetailsOut, tags=["movie_details"])
async def get_all_details():
    """Get all movie details of all movies in the database"""
    pass


@movie_details_router.get('/api/movie_details/{movie_details_uuid}', response_model=MovieDetailsOut, tags=["movie_details"])
async def get_movie_details(movie_details_uuid: UUID4):
    """Get a specific movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    pass


@movie_details_router.post('/api/movie_details/', response_model=MovieDetailsOut, tags=["movie_details"])
async def add_movie_details(details: MovieDetails):
    """Add a new movie"""
    pass


@movie_details_router.delete('/api/movie_details/{movie_details_uuid}', response_model=CustomeMessages, tags=["movie_details"])
async def remove_movie(movie_details_uuid: UUID4):
    """Remove a movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    # return CustomeMessages('Movie details has been successfully deleted')
    pass


@movie_details_router.patch('/api/movie_details/{movie_details_uuid}', response_model=MovieDetailsOut, tags=["movie_details"])
async def edit_movie(movie_details_uuid: UUID4):
    """Edit movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    pass
