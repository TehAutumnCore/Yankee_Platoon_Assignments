from django.test import TestCase
from django.core.exceptions import ValidationError
from move_app.models import Pokemon
from move_app.models import Move

# Create your tests here.

class PokemonTest(TestCase):
    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name="Squirtle", description='A very bubbly turtle with a spicy personality')
        try:
            new_pokemon.full_clean()
            self.assertIsNotNone(new_pokemon)
        except ValidationError as v:
            print(v.message_dict)
            self.fail()
            
    def test_02_create_pokemon_with_incorrect_name_format(self):
        new_pokemon = Pokemon(name="Squ1rtle", description='A very bubbly turtle with a spicy personality')
        try:
            new_pokemon.full_clean()
        except ValidationError as v:
            self.assertTrue("Improper name format." in v.message_dict['name'])
            
# -------------------MOVE MODEL TESTS--------------------------

# Create your tests here.

class MoveTest(TestCase):
    def test_01_create_pokemon_instance(self):
        new_move = Move(name="Psychic")
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as v:
            print(v.message_dict)
            self.fail()
            
    def test_02_move_with_incorrect_name(self):
        new_move = Move(name="wing 4ttack")
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as v:
            self.assertTrue("Improper Move Name Format." in v.message_dict['move_name'])