from typing import Optional
from models.movies import Movies, MovieOut
from fastapi import FastAPI
movie_api = FastAPI()


@movie_api.get('/api/1/movies/')
async def get_all_movies():
    return {'name': 'Welcome', 'rate': 7.5}


@movie_api.post('/api/1/movies/add_movie/', response_model=Movies, response_model_exclude={'id'})
async def add_movie(movie: Movies):
    return movie
    