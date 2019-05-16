from .models.game import Game
from .models.guess import Guess
from rest_framework import serializers


# Serializer for game_list get and post (when no data is received)
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'state',)

# Serializer for a game_list when post is received with data
class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'state', 'c1', 'c2', 'c3', 'c4')

# Serializer for a guess
class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = ('id', 'c1', 'c2', 'c3', 'c4', 'black_pegs', 'white_pegs', 'game_id')
