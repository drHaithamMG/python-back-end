from django.urls import path, include
from .views import *
urlpatterns = [
    path('1/get_movies_list',get_movie_list,name='movies_list_api'),
    path('1/get_movie_details/<uuid:uuid>',get_movie_details,name='movie_details_api')
    ]
