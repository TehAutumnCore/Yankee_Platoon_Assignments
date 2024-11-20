from django.urls import path
from .views import AllBrawlers, SingleBrawler

urlpatterns = [
    path('', AllBrawlers.as_view(), name='all_brawl_stars'),
    path('',SingleBrawler.as_view(),name='single_brawler')
]