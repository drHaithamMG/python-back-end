from fastapi import FastAPI, HTTPException
from pydantic import UUID4
from src.controller.movie_controller import movies_router
from src.controller.movie_details_controller import movie_details_router

tags_metadata = [
    {
        "name": "movies",
        "description": "Get movies/Add movie/Edit movie/Delete movie",
    },
    {
        "name": "movie_details",
        "description": "Get movie details/Add movie details/Edit movie details/Delete movie details ",
    },
]

movies_api = FastAPI(title='H-movies API', openapi_tags=tags_metadata)
movies_api.include_router(movies_router)
movies_api.include_router(movie_details_router)
