from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Game
from .serializers import GameSerializer
from django.shortcuts import get_object_or_404
from .steam_api import get_action_games  # Add this import at the top

class GameViewAll(APIView):
    def get(self, request):
        try:
            print("Starting game fetch")
            steam_games = get_action_games()
            print(f"Got {len(steam_games)} games from Steam")
            
            games = []
            for game_data in steam_games:
                print(f"Processing game: {game_data}")
                game, created = Game.objects.update_or_create(
                    steam_app_id=game_data['steam_app_id'],
                    defaults=game_data
                )
                games.append(game)
            
            print(f"Total games saved: {len(games)}")
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            print(f"Error in GameViewAll: {str(e)}")
            return Response(
                {"error": "Failed to fetch games"}, 
                status=HTTP_400_BAD_REQUEST
            )
    
    
    # POST 127.0.0.1:8000/api/v1/games/
    # {
    # "title": "Game Title",
    # "description": "Game Description",
    # "genre": "Game Genre",
    # "price": 59.99,
    # "sale": False,
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
    # "sake": True
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