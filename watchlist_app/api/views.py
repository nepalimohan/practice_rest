from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@api_view()
def movie_details(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializers = MovieSerializer(movies)
    return Response(serializers.data)
    