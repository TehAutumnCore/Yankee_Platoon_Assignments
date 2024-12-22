from django.db import models
from user_app.models import User
from game_app.models import Game

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews') #Foreign key to User model
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews') #Foreign key to Game model
    review_text = models.TextField() #The actual review content
    rating = models.IntegerField() #User's rating for the game
    created_at = models.DateTimeField(auto_now_add=True) #When the review was created
    updated_at = models.DateTimeField(auto_now=True) #When the review was last updated

    class Meta:
        unique_together = ['user', 'game'] #A user can only review a game once

    def __str__(self):
        return f"{self.user.email}'s review of {self.game.title}"