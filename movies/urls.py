from django.urls import path
from . import views

# print("movies/urls.py: path('', views.index, name='index')")
urlpatterns = [
    path('', views.index, name='index'),
]
