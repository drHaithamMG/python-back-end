from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
movies = [
    {
        'title': 'A',
        'link': 'https://www.google.com'

    }
]


def home(request):
    context = {
        'title': 'Home',
        'movies': movies
    }
    return render(request, 'movies/home.html', context=context)


def movie_details(request, id):
    movie = models.Movies.objects.get(id)
    print(movie)
    # return render(request, 'movies/details.html', context=...)
    return HttpResponse('Under Development...')
