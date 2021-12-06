from django.contrib import admin
from .models import Movie
# Register your models here.

@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','active']