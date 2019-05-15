from __future__ import unicode_literals

from django.db import models


class Color(models.Model):
    """
    Different colors available
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Game(models.Model):
    """
    Handles the game itself
    """
    id = models.CharField(max_length=10, primary_key=True)
    state = models.CharField(choices=(
        (0, 'finished'),
        (1, 'ongoing')
    ), max_length=20)
    color_ids = models.ManyToManyField(Color)

    @classmethod
    def create(cls):
        game = cls(id=1, state=1)
        return game
