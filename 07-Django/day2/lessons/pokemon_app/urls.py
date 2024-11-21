from django.urls import path, register_converter
from .views import AllPokemon, SinglePokemon
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    #http://127.000.000/api/v1/pokemon/

    path('', AllPokemon.as_view(), name='all_pokemon'),
    #http://127.000.000/api/v1/pokemon/pikachu/
    path('<int_or_str:single_pokemon>/', SinglePokemon.as_view(), name='single_pokemon')
]








"""
const newPokemon = {
    name: "Charmander",
    types: "Fire",
    description: "A pokemon that prefers hot places."
};


axios.post('http://127.0.0.1:8000/api/v1/pokemon/', newPokemon)
    .then(response => {
        console.log("New Pokemon created:", response.data);
    })
    
    """