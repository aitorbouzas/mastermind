from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.game import Game
from ..serializers import GameSerializer, GameDetailSerializer


class GameList(APIView):

    # GET LIST OF GAMES
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    # CREATE NEW GAME
    def post(self, request, format=None):
        return_status = status.HTTP_400_BAD_REQUEST
        # If data is provided, it means that it has colors, so we should check
        if request.data:
            values = {
                'state': 1,
                'c1': request.data.get('c1'),
                'c2': request.data.get('c2'),
                'c3': request.data.get('c3'),
                'c4': request.data.get('c4'),
            }
            serializer = GameDetailSerializer(data=values)

            if serializer.is_valid():
                serializer.save()
                result = serializer.data
                return_status = status.HTTP_200_OK
            else:
                result = serializer.errors
        else:
            # Calling create without parameters should create a random game
            game = Game.create()

            # We serialize it with GameSerializer so it doesn't tells you it's colors
            serializer = GameSerializer(game)
            result = serializer.data
            return_status = status.HTTP_200_OK
        return Response(result, status=return_status)
