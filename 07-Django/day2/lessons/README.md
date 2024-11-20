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


scratch = Move.objects.get(name = 'Scratch')
scratch
<Move : 70 20 70>
ser_scratch = MoveSerializer(scratch)
ser_scratch
moveSerializer(<Move> id= name = accuracy =pp=power)
ser_scratch.data
{id:  name: }
serializeMove.is_valid()
serializedMove.save()

request_data = {"name": ,"accuracy":}
ser_flame_thrower = MoveSerializer(data=request_data)
ser_flame_thrower.isvalid()


# DJANGO Server
-python manage.py runserver
-127.0.0.1:8000/admin   <!-- from urls.py in pokedex_proj-->
-urls.py    
-from django.http import HttpResponse

create a "view" with 
    def blah_view(request):
        pass
        return HttpResponse(pass)

update urlpatters=[
    path('admin/', admin.site.urls),
    path('sameple_endpoint/', func_sample_view)
]

# Restful API and API Views
views.py and urls.py 
django.urls import path, include

in urls.py you create the endpoint(s) and use include to link the main urls.py to the other app.urls.py where youll create all the related endpoints there. 

    This will take place in pokemon_app urls where youll put the related views
    path('api/v1/pokemon/', include("pokemon_app.urls")),

    This will take place in move_app urls where youll put the related views
    path('api/v1/moves', include("move_app.urls"))

then create a class that gets all pokemon(objects.all()), then create a class where it recieves just one(objects.get()).

# Converters.py
views/url


# Testing Views
creating a tests folder

python manage.py test tests

# create a new app called api_app
add the api_app 
pip freeze > requirements
create a view for this application and connect the view to the app
pip install requests
pip install OAuthlib
pip install python-env
touch .env .gitignore

in settings.py of proj
from dotenv import dotenv_values

env = dotenv_values(".env") #sets where to reference or look for the env info(.env)

<!-- shell -->
from django.core.management.utils import get_random_secret_key
new_key = get_random_secret_key()
new_key

import pprint formats the json into readable format in the console
python manage.py makemigrations
python manage.py migrate

<!-- mimicks 3rd party -->
from unittest.mock import patch
from rest_framework.test import APIClient