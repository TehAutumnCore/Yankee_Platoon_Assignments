from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User

# Create your views here.

class SignUp(APIView):
    pass

class LogIn(APIView):
    pass

class LogOut(APIView):
    pass

class Info(APIView):
    pass