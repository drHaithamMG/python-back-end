from fastapi import FastAPI, HTTPException
from pydantic import UUID4
from models.pydantic.movies import Movie, MovieOut, CustomeMessages
from models.pydantic.movie_details import MovieDetails, MovieDetailsOut

movies_api = FastAPI(title='H-movies API')

# movie_routs


@movies_api.get('/api/movies')
async def get_all():
    """Get all movies from database"""
    pass


@movies_api.get('/api/movies/{movie_uuid}')
async def get_movie(movie_uuid: UUID4):
    """Get a specific movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass


@movies_api.post('/api/movies/', response_model=MovieOut)
async def add_movie(movie: Movie):
    """Add a new movie"""
    pass


@movies_api.delete('/api/movies/{movie_uuid}', response_model=CustomeMessages)
async def remove_movie(movie_uuid: UUID4):
    """Remove a movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')

    # return CustomeMessages('Movie has been successfully deleted')
    pass


@movies_api.patch('/api/movies/{movie_uuid}', response_model=MovieOut)
async def edit_movie(movie_uuid: UUID4):
    """Edit movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass

# --------------------------------------------------------------------------
# movie_details_routs


@movies_api.get('/api/details_list', response_model=MovieDetailsOut)
async def get_all_details():
    """Get all movie details of all movies in the database"""
    pass


@movies_api.get('/api/movie_details/{movie_details_uuid}', response_model=MovieDetailsOut)
async def get_movie_details(movie_details_uuid: UUID4):
    """Get a specific movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    pass


@movies_api.post('/api/movie_details/', response_model=MovieDetailsOut)
async def add_movie_details(details: MovieDetails):
    """Add a new movie"""
    pass


@movies_api.delete('/api/movie_details/{movie_details_uuid}', response_model=CustomeMessages)
async def remove_movie(movie_details_uuid: UUID4):
    """Remove a movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    # return CustomeMessages('Movie details has been successfully deleted')
    pass


@movies_api.patch('/api/movie_details/{movie_details_uuid}', response_model=MovieDetailsOut)
async def edit_movie(movie_details_uuid: UUID4):
    """Edit movie details passed on details's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie details not found')
    pass
