from django.db import models
from user_app.models import User
from game_app.models import Game

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libraries')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='libraries')
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'libraries'
        unique_together = ['user', 'game']

    def __str__(self):
        return f"{self.user.display_name}'s library - {self.game.title}"