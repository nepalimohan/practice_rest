from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers = MovieSerializer(movies)
        return Response(serializers.data)
    
    if request.method == 'PUT':
        movies = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movies, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    