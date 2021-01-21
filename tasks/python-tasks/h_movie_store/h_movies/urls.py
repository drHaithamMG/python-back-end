from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home_page'),
    # Extra feature , adding search
    # path('search/<uuid>', views.home, name='home_page'),
    path('movie/details/<uuid:uuid>', views.movie_details, name='movie_details'),
    path('movie/add', views.add_new_movie, name='movie_new'),
    path('movie/edit/<uuid:uuid>', views.movie_edit, name='movie_edit'),
    path('movie/delete/<uuid:uuid>', views.movie_delete, name='movie_delete'),

]
