from __future__ import unicode_literals

from django.db import models
from .game  import Game


class Guess(models.Model):
    """
    Handles a guess, it relates to a game and has a result
    """
    id = models.AutoField(primary_key=True)

    # TODO
    # Colors are a bit ugly this way, I know. They should be saved in another model and create a many2many relation
    c1 = models.CharField(max_length=10)
    c2 = models.CharField(max_length=10)
    c3 = models.CharField(max_length=10)
    c4 = models.CharField(max_length=10)

    # Result
    black_pegs = models.IntegerField()
    white_pegs = models.IntegerField()

    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    @classmethod
    def create(cls, values):
        game = Game.objects.get(id=values.get('game_id'))
        if not game or game.state != 1:
            return {}
        black_pegs = 0
        white_pegs = 0

        # We save two lists, a guess list and a solution list
        guess = [values.get('c1'), values.get('c2'), values.get('c3'), values.get('c4')]
        solution = [game.c1, game.c2, game.c3, game.c4]
        i = 0

        for color in guess:
            indices = [i for i, x in enumerate(solution) if x == color]
            for j in indices:
                if j == i:
                    black_pegs += 1
                    solution[i] = None
                elif solution[j] != guess[j]:
                    white_pegs += 1
                    solution[j] = None
                    continue
            i += 1

        # TODO
        # Make color count dynamic so it can scale
        # If there are 4 black pegs, it means the game's over
        if black_pegs == 4:
            game.state = 0
            game.save()

        instance = cls(
            game_id=game,
            c1=values.get('c1'),
            c2=values.get('c2'),
            c3=values.get('c3'),
            c4=values.get('c4'),
            black_pegs=black_pegs,
            white_pegs=white_pegs,
        )
        instance.save()
        return instance
