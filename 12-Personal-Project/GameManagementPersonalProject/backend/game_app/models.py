from django.db import models
from django.core import validators as v
# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255) #game title
    description = models.TextField(blank=True, null=True) #game description
    genre = models.CharField(max_length=100, blank=True, null=True) #game genre
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) #game price
    sale = models.BooleanField(default=False)
    image_url = models.URLField(blank=True, null=True) #game thumbnail image
    steam_app_id = models.CharField(max_length=50, unique=True) #Steam App ID, each game has its own App ID
    cached_at = models.DateTimeField(auto_now=True) #cache timestamp for updates, when game was last updated in db
    
    def __str__(self):
        return self.title