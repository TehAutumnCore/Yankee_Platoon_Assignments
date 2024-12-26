from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from .models import Library
from .serializers import LibrarySerializer
from game_app.models import Game
from django.shortcuts import get_object_or_404

class LibraryViewAll(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_library = Library.objects.filter(user=request.user)
        serializer = LibrarySerializer(user_library, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        print("Request data received:", request.data)
        game_id = request.data.get('game')
        
        if not game_id:
            return Response({"error": "Game ID is required"}, status=HTTP_400_BAD_REQUEST)

        # Create the full data dictionary
        data = {
            'user': request.user.id,
            'game': game_id
        }
        print("Data being sent to serializer:", data)
        
        # First check if game exists
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=HTTP_400_BAD_REQUEST)

        # Check if already in library
        if Library.objects.filter(user=request.user, game=game).exists():
            return Response({"error": "Game already in library"}, status=HTTP_400_BAD_REQUEST)

        # Create the library entry
        try:
            library_item = Library.objects.create(
                user=request.user,
                game=game
            )
            serializer = LibrarySerializer(library_item)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            print("Error creating library item:", str(e))
            return Response({"error": "Failed to add game to library"}, status=HTTP_400_BAD_REQUEST)

class LibraryViewDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        # Find the library entry for this game and user
        library_item = get_object_or_404(
            Library, 
            game_id=id,
            user=request.user
        )
        library_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)