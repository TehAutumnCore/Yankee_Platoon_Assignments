from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    account_type = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(max_length=255, unique=True,null=False,blank=False)
    active = models.BooleanField(default=False,null=False,blank=False)
    
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255,null=False,blank=False,unique=True)
    in_stock = models.IntegerField(default=0,blank=False) #boolean?
    rating = models.CharField(max_length=255,null=False,blank=False)
    
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.IntegerField(null=False,blank=False)
    middle_init = models.IntegerField(null=False,blank=True)
    age = models.IntegerField(null=False,blank=False)
    
class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=255,null=False,blank=False)
    zipcode = models.IntegerField(null=False,blank=False)
    state = models.CharField(null=False,blank=False)
    appt_num = models.IntegerField(null=False,blank=False)
    
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False,blank=False)
    number_of_employees = models.IntegerField(default=1,null=False,blank=False)
    rating = models.FloatField(null=False,blank=False)
    owner = models.IntegerField(unique=True,null=False,blank=False)