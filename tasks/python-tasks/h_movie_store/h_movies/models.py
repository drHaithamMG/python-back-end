from django.db import models
from django.db import models
import uuid


class Movies(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False, auto_created=True)
    name = models.CharField(max_length=100, null=False)
    production_date = models.DateTimeField(null=True)
    rate = models.FloatField(default=0.0, null=True)
    pic = models.CharField(max_length=500, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    movie_detail_id = models.ForeignKey(
        'MovieDetails', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MovieDetails(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False, auto_created=True)
    catagorie = models.CharField(max_length=100, null=True)
    production_company = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0.0, null=False)
    overview = models.TextField(max_length=200, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.movie = Movies.objects.get(movie_detail_id_id=self.id)
        return f'{self.movie.name} details'
