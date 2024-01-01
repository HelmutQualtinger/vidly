from django.contrib import admin
from .models import Movie, Genre
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year',
                    'number_in_stock', 'daily_rate', 'genre', 'date_changed')
    exclude = ('date_changed',)


admin.site.register(Movie, MovieAdmin)

admin.site.register(Genre, GenreAdmin)
