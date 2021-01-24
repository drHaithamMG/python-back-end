from fastapi import HTTPException
from pydantic import UUID4
from . import movies_api
# routs


@movies_api.get('/api/1/movies_list')
async def get_all():
    """Get all movies from database"""
    pass


@movies_api.get('/api/1/movies/{movie_uuid}')
async def get_movie(movie_uuid:UUID4):
    """Get a specific movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass


@movies_api.post('/api/1/movies/')
async def add_movie():
    """Add a new movie"""
    pass


@movies_api.delete('/api/1/movies/{movie_uuid}')
async def remove_movie(movie_uuid:UUID4):
    """Remove a movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass


@movies_api.put('/api/1/movies/{movie_uuid}')
async def edit_movie(movie_uuid:UUID4):
    """Edit movie passed on movie's uuid"""
    # try:

    # except:
    #     raise HTTPException(status_code=404,detail='Movie not found')
    pass
