from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255, unique=True)
    level = models.IntegerField(default=1)
    date_encountered = models.DateField(default='2015-01-01')
    captured = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {'Has been captured' if self.captured else 'Not yet captured'}"
    
    def level_up_pokemon(self):
        self.level +=1