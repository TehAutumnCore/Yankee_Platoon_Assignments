from django.test import TestCase
from django.core.exceptions import ValidationError
from pokemon_app.models import Pokemon
from move_app.models import Move

# Create your tests here.
class PokemonTest(TestCase):

    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name='Squirtle', description='A very bubbly turtle with a spicy personality')
        
        try:
            new_pokemon.full_clean()
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()

    def test_02_create_pokemon_with_incorrect_name_format(self):
        new_pokemon = Pokemon(name='Squ1rtle', description='A very bubbly turtle with a spicy personality')
        try:
            new_pokemon.full_clean()
        except ValidationError as e:
            self.assertTrue('Improper name format.' in e.message_dict['name'])


#--------------------------------- MOVE MODEL TESTS
class MoveTest(TestCase):

    def test_01_create_move_instance(self):
        # create a move
        new_move = Move(name='Psychic')
        #ensure its created, full.clean(),
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()

        #if NOT clean, self.fail


    #test our validator
    def test_02_create_move_with_incorrect_name(self):
        new_move = Move(name='w1ng 4ttack')

        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            self.assertTrue('Improper Move Name Format.' in e.message_dict["name"])