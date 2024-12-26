from rest_framework import serializers
from .models import Library
from game_app.serializers import GameSerializer
from game_app.models import Game

class LibrarySerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = Library
        fields = ['id', 'user', 'game', 'added_at']
        read_only_fields = ['added_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['game'] = GameSerializer(instance.game).data
        return representation