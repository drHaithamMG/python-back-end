from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Movies, MovieDetails
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    movies = Movies.objects.all()
    context = {
        'title': 'Home',
        'movies': movies,
    }
    return render(request, 'h_movies/home.html', context=context)


def movie_details(request, uuid):
    try:
        movie = Movies.objects.get(id=uuid)
        if request.method == 'GET':
            context = {
                'title': movie.name,
                'movie': movie
            }
            return render(request, 'h_movies/details.html', context=context)
    except Movies.DoesNotExist:
        raise Http404('movie does not exist')


def check_if_exists(movie_name):
    try:
        Movies.objects.get(name=movie_name)
    except ObjectDoesNotExist:
        return False
    return True


def add_new_movie(request):
    if request.method == 'POST':
        response = request.POST
        name = response.get('name')
        if check_if_exists(name):
            return render(request, 'h_movies/add.html', context={
                'title': 'Add new movie',
                'alert': 'Movie already exists'
            })
        else:
            movie_detail = MovieDetails()
            movie_detail.catagorie = response.get('catagorie')
            movie_detail.production_company = response.get('pcompany')
            movie_detail.price = response.get('price')
            movie_detail.overview = response.get('overview')
            movie_detail.save()
            movie = Movies()
            movie.movie_detail_id = MovieDetails(movie_detail.id)
            movie.name = response.get('name')
            movie.production_date = response.get('pdate')
            movie.rate = response.get('rate')
            movie.pic = response.get('picurl')
            if not movie.pic:
                movie.pic = "https://image.winudf.com/v2/image/Y29tLmZyZWVtb3ZpZXNfZnVsbG1vdmllc19tb3ZpZWFwcF9uZXdtb3ZpZV9tb3ZpZXNmcmVlLm1vdmllc19tb3ZpZXNhcHBfb25saW5lbW92aWVfbW92aWVkb3dubG9hZF9mcmVlX21vdmllX2ljb25fMTUzNTM1ODQ1M18wMTQ/icon.png?w=170&fakeurl=1"
            movie.save()
            messages.success(
                request, f'{movie.name} has been successfully added')
            return redirect('/')

    else:
        return render(request, 'h_movies/add.html', context={
            'title': 'Add new movie',
        })


def movie_edit(request, uuid):

    movie = Movies.objects.get(id=uuid)
    context = {
        'title': movie.name,
        'movie': movie
    }
    if request.method == 'POST':
        response = request.POST
        changes = False
        movie_detail = MovieDetails.objects.get(
            id=movie.movie_detail_id_id)

        if not movie_detail.catagorie == response.get('catagorie'):
            movie_detail.catagorie = response.get('catagorie')
            changes = True
        if not movie_detail.production_company == response.get('pcompany'):
            movie_detail.production_company = response.get('pcompany')
            changes = True

        if not movie_detail.price == response.get('price'):
            movie_detail.price = response.get('price')
            changes = True

        if not movie_detail.overview == response.get('overview'):
            movie_detail.overview = response.get('overview')
            changes = True
        if changes == True:
            movie_detail.save()
        edited_movie = movie
        changes = False
        if not edited_movie.name == response.get('name'):
            changes = True
            edited_movie.name = response.get('name')
        if not edited_movie.production_date == response.get('pdate'):
            changes = True
            edited_movie.production_date = response.get('pdate')
        if not edited_movie.rate == response.get('rate'):
            changes = True
            edited_movie.rate = response.get('rate')
        if not edited_movie.pic == response.get('picurl'):
            changes = True
            edited_movie.pic = response.get('picurl')
            if not edited_movie.pic:
                edited_movie.pic = "https://image.winudf.com/v2/image/Y29tLmZyZWVtb3ZpZXNfZnVsbG1vdmllc19tb3ZpZWFwcF9uZXdtb3ZpZV9tb3ZpZXNmcmVlLm1vdmllc19tb3ZpZXNhcHBfb25saW5lbW92aWVfbW92aWVkb3dubG9hZF9mcmVlX21vdmllX2ljb25fMTUzNTM1ODQ1M18wMTQ/icon.png?w=170&fakeurl=1"
        if changes == True:
            edited_movie.save()
            messages.success(
                request, f'{movie.name} has been successfully modified')
            return redirect('/')
    else:
        return render(request, 'h_movies/edit.html', context={
            'title': 'Edit movie',
            'movie': movie
        })


def movie_delete(request, uuid):
    try:
        movie = Movies.objects.get(id=uuid)
        movie_name = movie.name
        if request.method == 'POST':
            MovieDetails.objects.filter(
                id=movie.movie_detail_id_id).delete()
            movies = Movies.objects.all()
            messages.success(
                request, f'{movie.name} has been successfully deleted')

            return redirect('/')
        else:
            return render(request, 'h_movies/delete.html', context={
                'title': movie.name,
                'movie': movie
            })
    except Movies.DoesNotExist:
        raise Http404("ID does not exist")


def error_404(request, exception):
    data = {'title': 'Error 404', 'message': 'Page not found'}
    return render(request, 'h_movies/errors.html', data)


def error_400(request,  exception):
    data = {'title': 'Error 400', 'message': 'Bad request'}
    return render(request, 'h_movies/errors.html', data)


def error_500(request):
    data = {'title': 'Error 500', 'message': 'Server error'}
    return render(request, 'h_movies/errors.html', data)
