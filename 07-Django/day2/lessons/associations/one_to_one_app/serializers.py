from rest_framework import serializers
from .models import Person, Profile

class ProfileSerializer(serializers.ModelSerializers):
    class Meta:
        model = Profile
        fields = ['person']

class PersonSerializer(serializers.ModelSerializers):
    profile = ProfileSerializer()
    class Meta:
        model = Person
        fields = ['id','name','profile']