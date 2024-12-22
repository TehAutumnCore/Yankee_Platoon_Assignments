from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Library
from .serializers import LibrarySerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LibraryViewAll(APIView):
    permission_classes = [IsAuthenticated] # Only authenticated users can access
    
    # GET 127.0.0.1:8000/api/v1/library/
    def get(self, request):
        # Get all games in the user's library
        user_library = Library.objects.filter(user=request.user)
        serializer = LibrarySerializer(user_library, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    # POST 127.0.0.1:8000/api/v1/library/
    # {
    # "game": 1  # game id to add to library
    # }
    def post(self, request):
        # Add the current user to the data before serializing
        data = request.data.copy()
        data['user'] = request.user.id
        
        serializer = LibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class LibraryViewDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    # DELETE 127.0.0.1:8000/api/v1/library/{id}/delete/
    def delete(self, request, id):
        # Ensure user can only delete games from their own library
        library_item = get_object_or_404(Library, pk=id, user=request.user)
        library_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)