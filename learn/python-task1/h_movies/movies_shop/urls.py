from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    # Extra feature , adding search
    # path('search/<uuid>', views.home, name='home_page'),
    # path('movies/<uuid>', views.home, name='home_page')
]
