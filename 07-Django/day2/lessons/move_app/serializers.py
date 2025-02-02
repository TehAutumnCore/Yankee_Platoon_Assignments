from rest_framework import serializers
from .models import Move

class MoveSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField()
    class Meta:
        model = Move
        fields = ['id', 'name', 'power', 'accuracy', 'pokemon']

    def get_pokemon(self, instance):
        pokemon = instance.pokemon.all()
        ser_pokemon = [x.name for x in pokemon]
        return ser_pokemon