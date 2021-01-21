from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (
    handler400, handler404, handler500
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('h_movies.urls')),
    path('api/',include('h_movies_api.urls'))

]
handler404 = 'h_movies.views.error_404'
handler400 = 'h_movies.views.error_400'
handler500 = 'h_movies.views.error_500'
