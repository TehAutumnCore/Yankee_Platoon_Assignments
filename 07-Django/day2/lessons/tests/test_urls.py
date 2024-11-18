from django.test import TestCase, Client
from django.urls import reverse
from pokemon_app.views import AllPokemon, SinglePokemon
from move_app.views import AllMoves, SingleMove

class TestsUrls(TestCase):
    def test_001_get_all_pokemon(self):
        
        url = resolve(reverse('all_pokemon'))
        
        with self.subTest():
            self.assertEquals(url.route, 'api/v1/pokemon/')
            
        self_assertTrue(url.func.view_class is AllPokemon)