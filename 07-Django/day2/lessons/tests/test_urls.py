from django.test import TestCase
from django.urls import reverse, resolve
from pokemon_app.views import AllPokemon, SinglePokemon
from move_app.views import AllMoves, SingleMove


class TestUrls(TestCase):

    def test_001_all_pokemon(self):

        url = resolve(reverse('all_pokemon'))

        with self.subTest():
            self.assertEquals(url.route, 'api/v1/pokemon/')
        
        self.assertTrue(url.func.view_class is AllPokemon)