from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,blank=False)
    age = models.IntegerField(blank=False)
    number_of_pets= models.IntegerField(default=0, null=True,blank=False)

class Cat(models.Model):
    id = models.IntegerField(primary_key=True)
    breed = models.CharField(max_length=255, null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    vaccinated = models.BooleanField(default=False, null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=255, null=False,blank=False)
    
class Bird(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    vaccinated = models.BooleanField(default=False, null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    species = models.CharField(max_length=255, null=False,blank=False)
    
class Dog(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    vaccinated = models.BooleanField(default=False, null=False,blank=False)
    breed = models.IntegerField(max_length=255, null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    
class Exotic_Animal(models.Model):
    id = models.IntegerField(primary_key=True)
    region_of_origin = models.CharField(max_length=255, null=False,blank=False)
    name = models.CharField(max_length=255, null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    type_of_animal = models.CharField(max_length=255, null=False,blank=False)
    vaccinated = models.BooleanField(default=False, null=False,blank=False)