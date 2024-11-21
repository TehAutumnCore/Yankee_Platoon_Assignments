from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Trainer(AbstractUser):
    email = models.EmailField(max_length=255, unique=True,verbose_name='email address') #verbo1se name creates a nickname for this field
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['date_of_birth', 'city']