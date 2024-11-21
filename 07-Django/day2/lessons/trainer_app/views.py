from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Trainer
from rest_framework.views import APIVIEW
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT

from rest_framework.authtoken.models import Token #allows to create instance of a token
from rest_framework.authentication import TokenAuthentication #only people with the token can perform certain views
from rest_framework.permissions import IsAuthenticated  #validates token is authenticated
# Create your views here.

class TokenReq():
    authentication_classes = [TokenAuthentication] #this view will be called
    permission_classes = [IsAuthenticated]
    

class SignUp(APIVIEW):
    
    def post(self, request):
        data = request.data.copy()
        data["username"] = request.data["email"]
        trainer = Trainer.objects.create_user(**data) #username=data['username']
        token = Token.objects.create(user=trainer)
        return Response({"trainer":trainer.email, "token":token.key},status=HTTP_201_CREATED)

class AdminUser(APIVIEW):
    
    def post(self,request):
        data = request.data.copy()
        data["username"] = request.data["email"]
        master_trainer = Trainer.objects.create(**data)
        master_trainer.is_staff = True
        master_trainer.is_superuser = True
        master_trainer.save()
        token = token.objects.create(user=master_trainer)
        return Response({"master_trainer": master_trainer.email, "token": token.key}, status=HTTP_201_CREATED)

class LogOut(TokenReq):
    
    def post(self,request):
        
        request.user.auth_token.delete() #when this method runs
        return Response(status=HTTP_204_NO_CONTENT)


class LogIn(APIVIEW):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        trainer = authenticate(username=email, password=password)
        if trainer:
            token, create = Token.objects.get_or_create(user=trainer)
            return Response({"token": token.key, "trainer": trainer.email})
        else:
            return Response("No trainer matching credentials", status=HTTP_404_NOT_FOUND)
        
        
class Info(APIVIEW):
    pass