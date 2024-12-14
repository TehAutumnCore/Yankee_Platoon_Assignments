from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators as v
from .validators import validate_email

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,validators=[validate_email])
    age = models.PositiveIntegerField(default=18, blank= True, validators=[v.MinValueValidator(18)])
    display_name = models.CharField(max_length=50, blank = True)
        
    USERNAME_FIELD = 'email' #requires the 'email field' as the username
    REQUIRED_FIELDS = [] #abstractuser class includes username and password by default
    
    
    def __str__(self):
        return self.email