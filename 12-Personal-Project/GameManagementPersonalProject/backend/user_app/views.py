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

class TokenReq(APIView):
    authentication_classes = [TokenAuthentication] #sets up token based authentication
    permission_classes = [IsAuthenticated] #requires users to be logged in for access


class SignUp(APIView):
    def post(self, request): #accepts data in the request body(usually JSON) for user creation
        data = request.data.copy() #retrieves data sent by the client such as the email and password, and craetes a mutable copy of the incoming data
        data['username'] = data['email'] #assigns the email into username
        new_user = User.objects.create_user(**data) #creates users with hashed passwords
        if new_user:
            token = Token.objects.create(user=new_user) #gengerates an authentication token for the newly created user
            return Response({"user": new_user.email, "token": token.key}) #returns the user's email and their token
        return Response("Invalid user credentials", status=HTTP_400_BAD_REQUEST) #if user creation fails send a 400 status code

# {                          axios request should look similar
#     "email": "GaryGary"                should return  {
#     "password": "RojasRojas"                user: aaaaa
# }                                           token: bbbb        }

# {
#     "user": "gary@email.com",
#     "token": "53c55bbf261372e2c498d817ffb53278716a27ae"
# }


class LogIn(APIView):
    def post(self, request):
        print("This is my login view")
        email = request.data.get("email") #extracts the email from the request body
        password = request.data.get("password") #extracts the password from the request body
        user = authenticate(username=email, password=password) #checks if the user with the provided credentials exist
        if user: #if user exist
            token, created = Token.objects.get_or_create(user=user) #retrieve token or create one if one doesn't exist
            return Response({"Token": token.key, "user": user.email}) #Returns the user's email and token
        return Response("No user matching credentials", status=HTTP_404_NOT_FOUND) #returns status 404 not found if user doesn't exist

# {                    127.0.0.1:8000/api/v1/users/login using JSON format with email and password in body
#     "email": "gary@email.com",
#     "password": "123"
# }


class LogOut(TokenReq): #inherits authentication classes and permission classes from the TokenReq classes
    def post(self, request):
        request.user.auth_token.delete() #Logs out the user by deleting their token
        return Response(status=HTTP_204_NO_CONTENT) #returns a status 204 no content after deleting their token

# Dont need information passed through body. Only need Headers with Key = Authorization and Value = Token abcdef1234asda



class Info(TokenReq): #scratch the code
    def get(self, request):
        return Response({"email": request.user.email,"age": request.user.age, "display_name": request.user.display_name}) #returns the email, age, and display name of the authenticated user
    
    def put(self, request):
        data = request.data.copy()#retrieves the data sent by the client and creates a mutable copy
        user = request.user #retrieves the request data and the current authenticated user
        print(user)
        if data.get('age'): #
            user.age = data.get('age') #grab the data from the body and pass through the serializers with partial= True, and run is_valid() or .full_clean() and .save() within a try and except 
            user.full_clean()
            user.save()
        if data.get('display_name'):
            user.display_name = data.get('display_name')
            user.full_clean()
            user.save()
        return Response({"age":user.age, "display_name": user.display_name})
    
    
        # current_password = data.get('password') #retrieves the password from the request data 
        # if current_password and data.get('new_password'): #verifies the current password
            # user = authenticate(username=user.username, password = current_password) #updates the password
        #     user.set_password(data.get('new_password')) #updates the password with the new password
        #     user.full_clean() #validates the user object 
        #     user.save() #saves the changes
        #     return Response({"email":user.email, "age": user.age, "display_name": user.display_name, "new_password": user.password}, status=HTTP_200_OK) #returns the updated user information(email, display_name, age, new_password)
        #Using Authorization and Token sadasdsad  get method should return 
# {
#     "email": "gary@email.com",
#     "age": 18,
#     "display_name": ""
# }