from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from tests.answers import single_pokemon, single_move, all_pokemon,all_moves
import json
from unittest.mock import patch
from rest_framework.test import APIClient

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
        
class NounProjectTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
    
    @patch('request.get') #intercepts calls for .get and replaces it with mock_get for the test
    def test_pokeball_img_api_view(self, mock_get):
        ball = 'pokeball'
        
        #correct response from our api for the noun project
        preview_url = "https://static.thenounproject.com/png/6645692-200.png"
        
        mock_response = type('MockResponse', (), {'json': lambda self: {'icon_url' : preview_url}})
        mock_get.return_value = mock_response()
        response = self.client.get(reverse('noun_project', args=[ball]))
        
        with self.subTest():
            self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content), preview_url)