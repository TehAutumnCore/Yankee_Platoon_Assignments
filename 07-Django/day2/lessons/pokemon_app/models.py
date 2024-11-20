from django.db import models
from django.utils import timezone
from django.core import validators as v
from .validators import validate_pokemon_name, validate_pokemon_type

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255, blank=False,null=False,validators=[validate_pokemon_name])
    level = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    date_encountered = models.DateField("2015-01-01")
    date_capture = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Unknown Pokemon", validators=[v.MinLengthValidator(7),v.MaxLengthValidator(150)])
    captured=models.BooleanField(default=False)
    types = models.CharField(default='normal', validators=[validate_pokemon_type])
    
    def __str__(self):
        return f"{self.name} {'Has been caught' if self.captured else 'Has not been caught'}"
    
    def level_up(self):
        self.level +=1
        self.full_clean()
        self.save()
        
    def change_caught_status(self):
        self.captured = not self.captured
        self.save()
        
    def change_name(self,new_name):
        self.name = new_name
        self.full_clean()