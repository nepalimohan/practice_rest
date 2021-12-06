from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        return Response(serializers.data)
    
    if request.method == 'POST':
        serializers = MovieSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

@api_view()
def movie_details(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializers = MovieSerializer(movies)
    return Response(serializers.data)
    