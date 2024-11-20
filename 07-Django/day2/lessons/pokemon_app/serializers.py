from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = ['id','name','level','moves','types']
        
    def get_moves(self,instance):
        moves = instance.moves.all()