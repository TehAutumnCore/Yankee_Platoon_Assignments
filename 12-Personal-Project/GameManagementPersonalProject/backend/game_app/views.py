from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Game
from .serializers import GameSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class GameViewAll(APIView):
    # GET 127.0.0.1:8000/api/v1/games/
    def get(self,request): #fetch all games, serialize the queryset, return serialized data
        all_games = Game.objects.all()
        serializer = GameSerializer(all_games, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    
    # POST 127.0.0.1:8000/api/v1/games/
    # {
    # "title": "Game Title",
    # "description": "Game Description",
    # "genre": "Game Genre",
    # "price": 59.99,
    # "image_url": "https://example.com/image.jpg",
    # "steam_app_id": "123456"
    # }
    def post(self,request):
        serializer= GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class GameViewDetail(APIView):
    # GET 127.0.0.1:8000/api/v1/games/{id}/
    def get(self, request, id): #id of the game
        game = get_object_or_404(Game, pk=id) #get the game or return 404
        serializer = GameSerializer(game) #serialize the game data
        return Response(serializer.data, status=HTTP_200_OK)
    
class GameViewUpdate(APIView): 
    # PUT 127.0.0.1:8000/api/v1/games/{id}/update/
    # {
    # "description": "Updated game description",
    # "price": 49.99
    # }
    def put(self, request, id):
         game = get_object_or_404(Game, pk=id)
         serializer = GameSerializer(game, data=request.data, partial=True) #only update the field passed
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=HTTP_200_OK)
         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
     
class GameViewDelete(APIView):
    #DELETE 127.0.0.1:8000/api/v1/games/{id}/delete/
    def delete(self,request,id):
        game = get_object_or_404(Game, pk=id) #get the game or return 404
        game.delete() #delete the game
        return Response(status=HTTP_204_NO_CONTENT) #Return 204 when deleted