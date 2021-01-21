import main
from fastapi import FastAPI

movie_api = FastAPI()


@movie_api.get('/api/1/movies')
def movies_list():
    return 'Worked'
