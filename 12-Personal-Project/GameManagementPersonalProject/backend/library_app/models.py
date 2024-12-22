from django.db import models
from user_app.models import User
from game_app.models import Game

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libraries')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='libraries')
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Ensure a user can't add the same game twice
        unique_together = ['user', 'game']
        verbose_name_plural = 'libraries'

    def __str__(self):
        return f"{self.user.email}'s library - {self.game.title}"