from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from move_app.models import Move
from .serializers import PokemonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


# Create your views here.
class AllPokemon(APIView):

    def get(self, request):
        all_pokemon = Pokemon.objects.all().order_by('id')
        serialized_all_pokemon = PokemonSerializer(all_pokemon, many=True)
        return Response(serialized_all_pokemon.data)
    
    def post(self, request):
        # request.data grabs the information from the body of the axios request
        body_data = request.data.copy() 

        new_pokemon = PokemonSerializer(data=body_data)
        if new_pokemon.is_valid():
            new_pokemon.save()
            return Response(new_pokemon.data, status=HTTP_201_CREATED)
        return Response(new_pokemon.errors, status=HTTP_400_BAD_REQUEST)
    

    #------------------------------------------------------------------------------------
class SinglePokemon(APIView):

    def get_pokemon(self, single_pokemon):
        if type(single_pokemon) == int:
            single_pokemon = get_object_or_404(Pokemon, id=single_pokemon) # Pokemon.objects.get(id=single_pokemon) ? single_pokemon = id || string
        else:
            single_pokemon = get_object_or_404(Pokemon, name=single_pokemon.title())
        return single_pokemon
    
    def update_moves(self, pokemon, list_of_move_ids):
        for move_id in list_of_move_ids:
            if get_object_or_404(Move, id=move_id):
                pokemon.moves.add(move_id)
                pokemon.save()



    def get(self, request, single_pokemon):
        a_pokemon = self.get_pokemon(single_pokemon)
        serialized_pokemon = PokemonSerializer(a_pokemon)
        return Response(serialized_pokemon.data)
    
    def put(self, request, single_pokemon):
        body_data = request.data.copy()

        pokemon = self.get_pokemon(single_pokemon)

        list_of_move_ids = body_data.get('list_of_moves') # -> returning NOne if the field does not exist  body_data['list_of_moves']  body_data.get('list_of_moves', 0)

        updated_pokemon = PokemonSerializer(pokemon, data=body_data, partial=True)


        if updated_pokemon.is_valid():
            if list_of_move_ids is not None:
                self.update_moves(pokemon, list_of_move_ids)
            updated_pokemon.save()
            return Response(updated_pokemon.data, status=HTTP_204_NO_CONTENT)
        return Response(updated_pokemon.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, single_pokemon):
        single_pokemon = self.get_pokemon(single_pokemon)
        single_pokemon.delete()
        return Response(status=HTTP_204_NO_CONTENT)