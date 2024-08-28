from django.http.response import datetime
from django.shortcuts import render


# Example usage


def movie_list(request):
    movies = [
        {"id": 1, "title": "The Notebook", "genre": "romance"},
        {"id": 2, "title": "John Wick", "genre": "action"},
        {"id": 3, "title": "La La Land", "genre": "romance"},
        {"id": 4, "title": "Mad Max: Fury Road", "genre": "action"},
    ]
    return render(request, "appone/movies.html", {"movies": movies})
