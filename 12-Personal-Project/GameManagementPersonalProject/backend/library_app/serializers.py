from rest_framework.serializers import ModelSerializer
from .models import Library
from game_app.serializers import GameSerializer

class LibrarySerializer(ModelSerializer):
    game = GameSerializer(read_only=True)
    
    class Meta:
        model = Library
        fields = '__all__'