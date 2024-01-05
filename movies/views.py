from django.shortcuts import render

from django.http import HttpResponse
from .models import Movie, Genre
# Create your views here.


def index(request):

    titles = "<br>".join([movie.title for movie in Movie.objects.all()])

    return HttpResponse(titles)
