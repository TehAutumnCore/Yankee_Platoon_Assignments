from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReviewViewAll(APIView):
    permission_classes = [IsAuthenticated] # Only authenticated users can access
    
    # GET 127.0.0.1:8000/api/v1/reviews/
    def get(self, request):
        # Get all reviews by the user
        user_reviews = Review.objects.filter(user=request.user)
        serializer = ReviewSerializer(user_reviews, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    # POST 127.0.0.1:8000/api/v1/reviews/
    # {
    # "game": 1,  # game id
    # "review_text": "Great game!",
    # "rating": 5
    # }
    def post(self, request):
        # Add the current user to the data before serializing
        data = request.data.copy()
        data['user'] = request.user.id
        
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ReviewViewUpdate(APIView):
    permission_classes = [IsAuthenticated]
    
    # PUT 127.0.0.1:8000/api/v1/reviews/{id}/update/
    # {
    # "review_text": "Updated review text",
    # "rating": 4
    # }
    def put(self, request, id):
        # Ensure user can only update their own reviews
        review = get_object_or_404(Review, pk=id, user=request.user)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ReviewViewDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    # DELETE 127.0.0.1:8000/api/v1/reviews/{id}/delete/
    def delete(self, request, id):
        # Ensure user can only delete their own reviews
        review = get_object_or_404(Review, pk=id, user=request.user)
        review.delete()
        return Response(status=HTTP_204_NO_CONTENT)