from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from game.models.game import Game
from game.serializers import GameSerializer


class GameDetail(APIView):

    # GET GAME HISTORY
    def get(self, request, id, format=None):
        return Response('')

    # POST A GUESS
    def post(self, request, id, format=None):
        return Response('')
