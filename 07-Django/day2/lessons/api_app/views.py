from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import request 
from requests_oauthlib import OAuth1
import pprint
# Create your views here.

class NounProject(APIView):
    def get(self, request):
        # auth = OAuth1("Key","Secret")
        auth = OAuth1(.env.get("NOUN_API_KEY"), env.get("NOUN_API_SECRET"))
        endpoint = f"https://api.thenounproject.com/v1/icon?query={types}&limit=1"
        
        response = requests.get(endpoint, auth = auth)
        # pp = pprint.PrettyPrinter(index = 2, depth=2)
        
        response_json = response.json()
        
        # pp.pprint(response_json)
        return Response(response_json['icons'][0]['thumbnail.url'])