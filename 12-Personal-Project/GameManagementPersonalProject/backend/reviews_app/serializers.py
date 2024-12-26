from rest_framework import serializers
from .models import Review
from game_app.serializers import GameSerializer

class ReviewSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        # Get the game ID from the view's game_id parameter
        game_id = self.context.get('game_id')
        if game_id:
            validated_data['game_id'] = game_id
        return super().create(validated_data)