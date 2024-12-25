from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db import IntegrityError
from .models import User

# Create your views here.
class SignUp(APIView):
    def post(self, request):
        try:
            data = request.data
            data['username'] = data['email']  # Set username to email
            new_user = User.objects.create_user(**data)
            token = Token.objects.create(user=new_user)
            return Response(
                {'token': token.key,
                'user': {
                    'id': new_user.id,
                    'email': new_user.email,
                    'display_name': new_user.display_name
                }}, 
                status=HTTP_201_CREATED
            )
        except IntegrityError as e:
            return Response(
                {'error': 'Email already exists'}, 
                status=HTTP_400_BAD_REQUEST
            )

class LogIn(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            user = authenticate(username=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {'token': token.key,
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'display_name': user.display_name
                    }},
                    status=HTTP_200_OK
                )
            return Response(
                {'error': 'Invalid Credentials'}, 
                status=HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=HTTP_400_BAD_REQUEST
            )

class LogOut(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Profile request received for user:", request.user)
        return Response({
            'email': request.user.email,
            'display_name': request.user.display_name,
            'age': request.user.age
        }, status=HTTP_200_OK)

    def put(self, request):
        try:
            user = request.user
            data = request.data

            if 'display_name' in data:
                user.display_name = data['display_name']
            if 'age' in data:
                user.age = data['age']

            user.save()

            return Response({
                'email': user.email,
                'display_name': user.display_name,
                'age': user.age
            }, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=HTTP_400_BAD_REQUEST
            )