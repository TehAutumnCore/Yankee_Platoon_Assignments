from rest_framework import serializers
from .models import Person, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['person']

class PersonSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Person
        fields = ['id', 'name', 'profile']