# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

import json


class CreateGameTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_game(self):
        # Send a post to create a game
        response = self.client.post('/game/')
        self.assertEqual(200, response.status_code)

        # Check game has a code and that it is ongoing
        result = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['state'], 1)

    def test_get_game(self):
        # Send a post to create 2 random games
        self.client.post('/game/')
        self.client.post('/game/')

        # Check there's a total of 2 games created
        response = self.client.get('/game/')
        result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(result), 2)

    def test_create_game(self):
        response = self.client.post('/game/', data={
            'colors': ["RED", "RED", "YELLOW", "GREEN"]
        })
        result = json.loads(response.content.decode('utf-8'))

        response = self.client.get('/game/' + result['id'])
