from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#didnt import requests_oatuhlib import OAuth1 because brawl_stars uses api_key and not oauth
import requests, pprint, json
from third_party_apis_proj.settings import env
# Create your views here.

class AllBrawlers(APIView):
    def get(self,request):
        # endpoint=f"https://api.brawlstars.com/v1/brawlers/160000{id}" #id: 1-85
        endpoint="https://api.brawlstars.com/v1/brawlers/?limit=5" #id: 1-85
        header = {
            "Authorization" : f"Bearer {env.get('BRAWL_STARS_API_KEY')}"
        }
        response = requests.get(endpoint, headers = header)
        
        response_json = response.json()
        return Response(response_json)
    
class SingleBrawler(APIView):
    def get(self,request,id):
        # endpoint=f"https://api.brawlstars.com/v1/brawlers/160000{id}" #id: 1-85
        endpoint=f"https://api.brawlstars.com/v1/brawlers/160000{id}" #id: 1-85
        header = {
            "Authorization" : f"Bearer {env.get('BRAWL_STARS_API_KEY')}"
        }
        response = requests.get(endpoint, headers = header)
        
        response_json = response.json()
        return Response(response_json)