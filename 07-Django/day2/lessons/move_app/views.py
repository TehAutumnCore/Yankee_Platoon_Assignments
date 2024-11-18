from django.shortcuts import render
from .models import Pokemon
from .serializers import PokemonSerializer
from .serializers import MoveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class AllMoves(APIView):
    all_moves = Moves.objects.all()
    all_moves = PokemonSerializer(Move.objects.all(), many = True)
    return Response(all_moves.data)
    
class SingleMove(APIView):
    def get(self, request, single_move):
        single_move = MoveSerializer(get_object_or_404(Move, name='single_move'.title()))
        return Response(single_move.data)