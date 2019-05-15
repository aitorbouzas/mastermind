from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Game
from .serializers import GameSerializer


class JSONResponse(HttpResponse):
    """
    Render HttpResponse into JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JSONResponse(serializer.data)
    if request.method == 'POST':
        game = Game.create()
        serializer = GameSerializer(game)
        return JSONResponse(serializer.data)