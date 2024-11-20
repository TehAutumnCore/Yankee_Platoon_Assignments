from django.db import models
from django.core import validators as v

# Create your models here.
class Brawler(models.Model):
    brawler_id = models.IntegerField(validators=[v.MinValueValidator(16000000), v.MaxValueValidator(16000087)]) #16,000,000 - 16,000,087
    name = models.CharField(max_length=255,blank=False,null=False) #validators=[validate_brawler_name]