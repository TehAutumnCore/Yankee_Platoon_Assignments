from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    
class Profile(models.model):
    bio = models.TextField(max_length=255)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)   #table has constaint FOREIGN KEY(person_id) REFERENCES one_to_one_app_person(id)
    
"""    
alice = Person(name='Alice')
alice.full_clean()
alice.save()
alice

alice_profile = Profile(bio='I am Alice', person=alice)
alice_profile.full_clean()
alice_profile.save()
alice
<Person: Person object(1)>

alice.name
'Alice'
alice_profile
<Profile: Object(1)>
alice_profile.bio
'I am alice'
alice_profile.person
<Person: Persom Object(1)>
alice_profile.person.name
'Alice'
alice.Profile
<Person: Persom Object(1)>
alice.profile.bio
'I am alice'
"""

"""
from one_to_one_app.serializers import ProfileSerializer, PersonSerializer
alice = Person.Objects.get(id=1)
alice_profile = Profile.objects.get(id=1)
alice

alice_profile
alice_profile
alice_profile.bio

ser_alice = PersonSerializer(alice)
ser_alice
ser_alice.data
ser_alice_profile = ProfileSerializer(alice_profile)
ser_alice_profile.data

"""

"""
from one_to_one_app.serializers import ProfileSerializer, PersonSerializer
alice = Person.objects.get(id=1)
alice
ser_alice = PersonSerializer(alice)
ser_alice.data

"""

"""
from one_to_one_app.serializers import ProfileSerializer, PersonSerializer
ser_alice = PersonSerializer(Person.objects.get(id=1))
ser_alice.data
"""