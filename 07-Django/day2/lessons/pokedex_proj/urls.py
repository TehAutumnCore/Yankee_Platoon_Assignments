"""
URL configuration for pokedex_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def square_area_view(request):
    area_of_square = 2 ** 2
    return HttpResponse(area_of_square)

def circle_area_view(request):
    print(request)
    area_of_circle = math.pi * (2 ** 2)
    return HttpResponse(area_of_circle)

def triangle_area_view(request):
    area_of_triangle = (height * base) / 2
    return HttpResponse(area_of_triangle)
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('squares/', square_area_view),
    path('circles/', circle_area),
    path('triangles/height/<int:height>/base/<int:base>', triangle_area_view) #returns 4.0
]