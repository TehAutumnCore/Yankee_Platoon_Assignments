from rest_framework.serializers import ModelSerializer
from .models import Review
from game_app.serializers import GameSerializer

class ReviewSerializer(ModelSerializer):
    game = GameSerializer(read_only=True) #nested serializer for game details
    
    class Meta:
        model = Review #uses the Review model from .models
        fields = '__all__' #includes all fields of the Review model