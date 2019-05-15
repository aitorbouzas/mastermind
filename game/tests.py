# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse

import json


class CreateGameTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_game(self):
        # Send a post to create a game
        response = self.client.post('/game/')
        self.assertEqual(200, response.status_code)

        # Check game has a code
        result = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(result['id'])

    def test_get_game(self):
        # Send a post to create 2 games
        self.client.post('/game/')
        self.client.post('/game/')

        # Check there's a total of 2 games created
        response = self.client.get('/game/')
        result = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(result), 2)
