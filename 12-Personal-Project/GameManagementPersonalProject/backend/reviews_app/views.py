from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ReviewViewAll(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, game_id):
        reviews = Review.objects.filter(game_id=game_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, game_id):
        data = {
            'user': request.user.id,
            'game': game_id,  # Make sure game_id is being passed
            'review_text': request.data.get('review_text'),
            'rating': request.data.get('rating')
        }
        
        print("Review data:", data)  # Debug print
        
        serializer = ReviewSerializer(data=data, context={'game_id': game_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
        print("Serializer errors:", serializer.errors)  # Debug print
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ReviewViewDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        # Update a specific review
        review = get_object_or_404(Review, id=id, user=request.user)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        # Delete a specific review
        review = get_object_or_404(Review, id=id, user=request.user)
        review.delete()
        return Response(status=HTTP_204_NO_CONTENT)