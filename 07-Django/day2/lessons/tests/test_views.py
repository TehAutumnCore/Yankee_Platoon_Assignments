from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from tests.answers import a_pokemon, a_move, all_pokemon, all_moves, updated_pokemon
import json
from unittest.mock import patch
from rest_framework.test import APIClient
from pokemon_app.models import Pokemon

class TestViews(TestCase):

    fixtures = [
        "pokemon_data.json",
        "move_data.json"
    ]

    def setUp(self):
        self.client = Client()

    def test_001_get_all_pokemon(self):
        response = self.client.get(reverse('all_pokemon'))

        response_body = json.loads(response.content)

        self.assertEqual(response_body, all_pokemon)


    def test_002_get_a_pokemon(self):
        
        response = self.client.get(reverse('single_pokemon', args=['pikachu']))

        response_body = json.loads(response.content)

        self.assertEqual(response_body, a_pokemon)

    def test_003_update_pokemon_data(self):
            body_data = {"level": 20, "captured": False, "description": "A fire type pokemon with an attitude"}
            
            response = self.client.put(reverse("single_pokemon", args=["charmander"]), data=body_data, content_type="application/json")

            self.assertEquals(response.status_code, 204)

    def test_004_create_pokemon(self):

        new_pokemon = {
         "name" : "Geodude",
         "level" : 22,
         "description": "Geodude is a rock type pokemon",
         "captured" : True   
        }

        response = self.client.post(reverse('all_pokemon'), new_pokemon, content_type='application/json')

        with self.subTest():
            self.assertEqual(response.status_code, 201)
        self.assertTrue('Geodude' == response.data.get('name'))

    def test_005_delete_pokemon(self):
        self.test_004_create_pokemon()

        response = self.client.delete(reverse('single_pokemon', args=['geodude']))
        self.assertEqual(response.status_code, 204)

class NounProjectTest(TestCase):

    def setUp(self):
        self.client = APIClient()


    @patch('requests.get')
    def test_pokeball_img_api_view(self, mock_get):
        ball = 'pokeball'

        #correct respect from our api for the nounproject
        preview_url = "https://static.thenounproject.com/png/6645692-200.png"

        mock_response = type(
                'MockResponse',
                (),
                {
                    'json': lambda self: {'icons': [{'thumbnail_url': preview_url}]},
                    'content': json.dumps({'thumbnail_url': preview_url}).encode('utf-8'),
                }
            )
        mock_get.return_value = mock_response()
        response = self.client.get(reverse('noun_project', args=[ball]))

        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), preview_url)