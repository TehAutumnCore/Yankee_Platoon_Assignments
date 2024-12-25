from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Library
from .serializers import LibrarySerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class LibraryViewAll(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_library = Library.objects.filter(user=request.user)
        serializer = LibrarySerializer(user_library, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        print("Request data:", request.data)
        print("User:", request.user.id)
        print("Game ID:", request.data.get('game'))

        if not request.data.get('game'):
            return Response(
                {'error': 'Game ID is required'}, 
                status=HTTP_400_BAD_REQUEST
            )

        data = {
            'user': request.user.id,
            'game': request.data.get('game')
        }

        print("Data being sent to serializer:", data)
        serializer = LibrarySerializer(data=data)
        
        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class LibraryViewDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        library_item = get_object_or_404(Library, pk=id, user=request.user)
        library_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)