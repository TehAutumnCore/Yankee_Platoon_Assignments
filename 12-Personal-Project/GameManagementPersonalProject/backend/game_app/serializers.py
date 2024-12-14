from rest_framework.serializers import ModelSerializer
from .models import Game

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game #uses the game model from .models
        fields = '__all__' #includes all fields of the game model