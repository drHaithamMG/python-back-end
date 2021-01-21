from django.shortcuts import render
from django.http import HttpResponse
from h_movies.views import *

def get_movie_list(request):
    return HttpResponse('Worked')


def get_movie_details(request, uuid):
    return HttpResponse(uuid)
