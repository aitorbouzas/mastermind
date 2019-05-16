from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.game import Game
from ..models.guess import Guess
from ..serializers import GuessSerializer


class GameDetail(APIView):
    # GET GAME HISTORY
    def get(self, request, id, format=None):
        game = Game.objects.get(id=id)
        guesses = Guess.objects.filter(game_id=game)
        ser_guesses = GuessSerializer(guesses, many=True)
        return Response(ser_guesses.data)

    # POST A GUESS
    def post(self, request, id, format=None):
        result = {}
        return_status = status.HTTP_400_BAD_REQUEST
        if request.data:
            values = {
                'game_id': id,
                'c1': request.data.get('c1'),
                'c2': request.data.get('c2'),
                'c3': request.data.get('c3'),
                'c4': request.data.get('c4'),
            }
            guess = Guess.create(values)
            if guess:
                serializer = GuessSerializer(guess)
                result = serializer.data
                return_status = status.HTTP_200_OK
        return Response(result, status=return_status)
