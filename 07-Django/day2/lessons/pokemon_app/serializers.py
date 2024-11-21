from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        exclude = ['date_captured']

    def get_moves(self, instance):
        moves = instance.moves.all()
        ser_moves = [move.name for move in moves]
        return ser_moves