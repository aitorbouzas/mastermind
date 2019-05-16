# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

import json


class CreateGameTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.validGameCreation = {
            'c1': "YELLOW",
            'c2': "RED",
            'c3': "RED",
            'c4': "GREEN"
        }
        self.invalidGameCreation = {
            'c1': "RED",
            'c2': "RED",
            'c3': "YELLOW",
        }

    def test_post_random_game(self):
        # Send a post to create a game
        response = self.client.post('/game/')
        self.assertEqual(200, response.status_code)

        # Check game has a code and that it is ongoing
        result = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['state'], 1)

    def test_post_specific_game(self):
        response = self.client.post('/game/', data=self.validGameCreation)
        result = json.loads(response.content.decode('utf-8'))

        # Assert response is 200
        self.assertEqual(200, response.status_code)

        # Assert colors are returned and wellformed
        self.assertEqual(result['c1'], self.validGameCreation['c1'])
        self.assertEqual(result['c2'], self.validGameCreation['c2'])
        self.assertEqual(result['c3'], self.validGameCreation['c3'])
        self.assertEqual(result['c4'], self.validGameCreation['c4'])

    def test_post_invalid_game(self):
        response = self.client.post('/game/', data=self.invalidGameCreation)

        # Assert response is 400
        self.assertEqual(400, response.status_code)

    def test_get_games(self):
        # Send a post to create 2 random games
        self.client.post('/game/')
        self.client.post('/game/')

        # Check there's a total of 2 games created
        response = self.client.get('/game/')
        result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(result), 2)

    def test_guess_game(self):
        # This is a preformed solution
        solution = {
            'c1': "YELLOW",
            'c2': "RED",
            'c3': "RED",
            'c4': "GREEN"
        }

        # This guess should result in two black pegs, and two white pegs
        guess = {
            'c1': "RED",
            'c2': "RED",
            'c3': "YELLOW",
            'c4': "GREEN"
        }

        response = self.client.post('/game/', data=solution)
        game = json.loads(response.content.decode('utf-8'))

        # TODO
        # Use reverse for views?
        response = self.client.post('/game/' + game.get('id'), data=guess)
        guess_result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(2, guess_result.get('black_pegs'))
        self.assertEqual(2, guess_result.get('white_pegs'))

    def test_resolve_game(self):
        # This is a preformed solution
        guess = solution = {
            'c1': "YELLOW",
            'c2': "RED",
            'c3': "RED",
            'c4': "GREEN"
        }

        response = self.client.post('/game/', data=self.validGameCreation)
        game = json.loads(response.content.decode('utf-8'))

        response = self.client.post('/game/' + game.get('id'), data=guess)
        guess_result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(4, guess_result.get('black_pegs'))
        self.assertEqual(0, guess_result.get('white_pegs'))

        # Make another guess after resolving it, it should give an error
        response = self.client.post('/game/' + game.get('id'), data=guess)
        self.assertEqual(400, response.status_code)

    def test_history_game(self):
        response = self.client.post('/game/', data=self.validGameCreation)
        game = json.loads(response.content.decode('utf-8'))
        guess1 = {
            'c1': "YELLOW",
            'c2': "RED",
            'c3': "RED",
            'c4': "GREEN"
        }
        guess2 = {
            'c1': "RED",
            'c2': "RED",
            'c3': "RED",
            'c4': "BLUE"
        }

        self.client.post('/game/' + game.get('id'), data=guess1)
        self.client.post('/game/' + game.get('id'), data=guess2)


        response = self.client.get('/game/' + game.get('id'))
        history = json.loads(response.content.decode('utf-8'))

        # History should contain two guesses
        self.assertEqual(2, len(history))
        for guess in history:
            self.assertEqual(guess1['c1'], guess.get('c1'))
            self.assertEqual(guess1['c2'], guess.get('c2'))
            self.assertEqual(guess1['c3'], guess.get('c3'))
            self.assertEqual(guess1['c4'], guess.get('c4'))
