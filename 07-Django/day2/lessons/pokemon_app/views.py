from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class AllPokemon(APIView):
    
    def get(self,request):
        all_pokemon = Pokemon.objects.all()
        serialized_all_pokemon = PokemonSerializer(all_pokemon, many=True)
        return Response(serialized_all_pokemon.data)
    
class SinglePokemon(APIView):
    
    def get(self,request,single_pokemon):
        #SELECT * FROM pokemon WHERE id = id
        #single_pokemon = get_object_or_404(Pokemon, id=id)
        if type(id) == int:
            single_pokemon = get_object_or_404(Pokemon, id=single_pokemon)
        else:
            single_pokemon = get_object_or_404(Pokemon, name = single_pokemon.id)
        serialized_Pokemon = PokemonSerializer(single_pokemon) #dont need many=true since its just a single pokemon
        return Reponse(serialized_Pokemon.data)