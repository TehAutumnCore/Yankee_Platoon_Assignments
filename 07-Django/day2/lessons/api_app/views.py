from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from pokedex_proj.settings import env
import pprint
# Create your views here.

class NounProject(APIView):

    def get(self, request, types):
        auth = OAuth1(env.get("NOUN_API_KEY"), env.get("NOUN_API_SECRET"))
        endpoint = f"https://api.thenounproject.com/v2/icon?query={types}&limit=1"

        response = requests.get(endpoint, auth=auth)
        # pp = pprint.PrettyPrinter(indent = 3, depth= 4)

        response_json = response.json()

        if 'icons' in response_json and response_json['icons']:
            return Response(response_json['icons'][0].get('thumbnail_url'))
        return Response({'error': 'No icons found'}, status=404)
        # pp.pprint(response_json)