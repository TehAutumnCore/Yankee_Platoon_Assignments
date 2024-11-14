# serializing 
blastoise = Pokemon(name='Blastoise', level=25)
blastoise.full_clean()
blastoise

from django.core.serializers import serialize
blastoise_ser = serialize("json",blastoise) returns object as a string
blastoise_ser <!-- returns the object as a string-->

import json
json_blastoise = json.loads(blastoise_ser) <!-- converts string into object -->
json_blastoise[0].get('fields')
blastoise.save()
blastoise
blastoise_ser = serialize("json",[blastoise])
blastoise_ser
json_blastoise = json.loads(blastoise_ser)
json_blastoise

# Django Rest Framework
pip install djangorestframework
freeze > requirements
update settings.py with the installed apps with rest_framework
created serializers.py in app

import Pokemon
from pokemon_app.serializers import PokemonSerializer
all_pokemon = Pokemon.objects.all()
all_pokemon
pikachu = Pokemon.objects.get(name='Pikachu)
pikachu
ser_pikachu = PokemonSerializer(pikachu)
ser_pikachu['pikachu']
ser_pikachu['name']
<BoundField value=Pikachu errors=None>


bulbasaur = pokemon.objects.get(name="Bulbasaur)
bulbasaur
ser_bulbasaur = PokemonSerializer(bulbasaur)
ser_bulbasaur
ser_bulbasaur['name']

serialized_pokemon = PokemonSerializer(all_pokemon,many=True)
serialized_pokemon
<PokemonSerializer(<QuerySet[<Pokemon: Pikachu has not been caught>, <Pokemon: blah>]>)>
ser_eevee = PokemonSerializer(data = eevee)
ser_eevee.save()
ser_eevee.is_valid()
ser_eevee.save()
<pokemon: Eevee Has not been caught>

ditto = {"name":"ditt0","level":20}
ser_ditto = PokemonSerializer(data=ditto)
ser_ditto.is_valid()
returns False

ditto = {"name":"ditto","level":20}
ser_ditto = PokemonSerializer(data=ditto)
ser_ditto.is_valid()
returns True


from django.core.serializers import serialize
blastoise = Pokemon.objects.get(name='Blastoise)
blastoise_serialized = serialize("json",[blastoise])
blastoise_serialized

import json
json_blastoise = json.loads(blastoise_serialized)
json_blastoise