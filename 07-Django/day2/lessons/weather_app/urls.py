from django.urls import path
from .views import TodaysWeather

urlpatterns = [
    path('', TodaysWeather.as_view(), name='todays_weather')
]