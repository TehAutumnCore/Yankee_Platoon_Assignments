from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pokedex_proj.settings import env
import requests
# Create your views here.


#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

class TodaysWeather(APIView):

    def get(self, request):
        api_endpoint = f"https://api.openweathermap.org/data/2.5/weather?q=austin&appid={env.get('WEATHER_API_KEY')}"
        response = requests.get(api_endpoint)

        response_json = response.json()

        return Response(response_json)