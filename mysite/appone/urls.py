from django.urls import include, path

from .views import (
    movie_list,
)

urlpatterns = [
    path("", movie_list),
]
