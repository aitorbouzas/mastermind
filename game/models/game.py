from __future__ import unicode_literals

import uuid
from django.db import models


class Game(models.Model):
    """
    Handles the game itself
    """
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=200)
    state = models.CharField(choices=(
        (0, 'finished'),
        (1, 'ongoing')
    ), max_length=20)
    c1 = models.CharField(max_length=10)
    c2 = models.CharField(max_length=10)
    c3 = models.CharField(max_length=10)
    c4 = models.CharField(max_length=10)

    @classmethod
    def create(cls, colors=False):
        if colors:
            game = cls(state="1", c1=colors[0], c2=colors[1], c3=colors[2], c4=colors[3])
        else:
            # TODO: get random colors if no colors are provided
            game = cls(state="1", c1="RED", c2="GREEN", c3="BLUE", c4="YELLOW")
        game.save()
        return game

    def __str__(self):
        return self.id
