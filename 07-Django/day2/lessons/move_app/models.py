from django.db import models
from django.core import validators as v
from .validators import validate_move_name
from pokemon_app.models import Pokemon

class Move(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, validators=[validate_move_name])
    accuracy = models.PositiveIntegerField(default=70,validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    pp = models.PositiveIntegerField(default=20, validators=[v.MinValueValidator(0), v.MaxValueValidator(35)])
    power = models.PositiveIntegerField(default=70, validators=[v.MinValueValidator(10), v.MaxValueValidator(120)])
    pokemon = models.ManyToManyField(Pokemon, related_name="moves") #can do manytomanyfield on either one, but has to be one or the other
    
    def __str__(self):
        return f"Name:{self.name} Accuracy:{self.accuracy} PP:{self.pp} power:{self.power}"