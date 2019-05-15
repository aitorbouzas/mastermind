from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from game.models.game import Game
from game.serializers import GameSerializer


class GameList(APIView):

    # GET LIST OF GAMES
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    # CREATE NEW GAME
    def post(self, request, format=None):
        # If colors data is provided, it means that maybe it has colors, so we should check
        if request.data:
            game = Game.create(colors=request.data.getlist('colors'))
        else:
            game = Game.create()
        serializer = GameSerializer(game)
        return Response(serializer.data)
