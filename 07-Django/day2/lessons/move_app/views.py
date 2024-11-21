from django.shortcuts import render, get_object_or_404
from .models import Move
from .serializers import MoveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class AllMoves(APIView):

    def get(self, request):
        all_moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(all_moves.data)
    
    def post(self, request):
        data = request.data.copy()
        new_move = MoveSerializer(data = data)
        if new_move.is_valid():
            new_move.save()
            return Response(new_move.data, status=HTTP_201_CREATED)
        return Response(new_move.errors, status=HTTP_400_BAD_REQUEST)
        # print(new_move)
    
    def delete(self, request, single_move):
        move = get_object_or_404(Move, id=single_move)
        move.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class SingleMove(APIView):

    def get(self, request, single_move):
        single_move = MoveSerializer(get_object_or_404(Move, name=single_move.title()))
        return Response(single_move.data)
    
    def put(self, request, single_move):
        body_data = request.data.copy()
        
        single_move = get_object_or_404(Move, id=single_move)
        # if data['power']:
        #     updated_move.power = data['power']    v- more dynamic
        updated_move = MoveSerializer(single_move, data=body_data, partial=True) #lets the serializer know that all the data to upodate the single move might not be present
        if updated_move.is_valid(): # if the updated move meets the validators requirements
            updated_move.save()
            return Response(updated_move.data, status= HTTP_200_OK) #defaults the status to 200 but put for visual
        print(updated_move)
        print(data)
        # return Response(True)
        return Response(updated_move.errors, status=HTTP_400_BAD_REQUEST)