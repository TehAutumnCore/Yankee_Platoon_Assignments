from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from tests.answers import single_pokemon, single_move, all_pokemon,all_moves
import json

class TestViews(TestCase):
    fixtures = [
        "pokemon_data.json",
        "move_data.json"
    ]
    
    def setUp(self):
        self.client = Client()
        
    def test_001_get_all_pokemon(self):
    # self.client = Client()
        response = self.client.get(reverse('all_pokemon')) #reverse is doing what axios does. takes an arugement(theview) and traces the view path. uses the related name to the path to grab everything
        response_body = json.loads(response.content) 
        self.assertEqual(response_body, all_pokemon)
    
    def test_002_get_a_pokemon(self):
        response = self.client.get(reverse('single_pokemon', args = ['pikachu']))
        response_body = json.loads(response.content)
        self.assertEqual(response_body, single_pokemon)