from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Library
from game_app.serializers import GameSerializer

class LibrarySerializer(ModelSerializer):
    game = GameSerializer(read_only=True)  # Add this line to include game details

    class Meta:
        model = Library
        fields = '__all__'
        read_only_fields = ('id',)
    
    def validate(self, data):
        if not data.get('user') or not data.get('game'):
            raise serializers.ValidationError("Both user and game are required")
        return data