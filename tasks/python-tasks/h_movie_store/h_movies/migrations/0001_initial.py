# Generated by Django 3.1.5 on 2021-01-17 15:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='f',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('catagorie', models.CharField(max_length=100)),
                ('production_company', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('overview', models.TextField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('production_date', models.DateTimeField(null=True)),
                ('rate', models.FloatField(default=0.0, null=True)),
                ('pic', models.CharField(max_length=500, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('movie_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='h_movies.moviedetails')),
            ],
        ),
    ]