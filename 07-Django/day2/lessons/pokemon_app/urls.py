from django.urls import path, register_converter
from .views import AllPokemon, SinglePokemon
from .converters import IntOrStrConverter
#takes in custom converter
register_converter[IntOrStrConverter, 'int_or_str']

urlpatterns = [ #127.0.0.1:8000/api/v1/Pokemon
    
    path('',AllPokemon.as_view(),name='all_pokemon'),
    path('<int_or_str:id>', SinglePokemon.as_view(),name='single_pokemon')
]