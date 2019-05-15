# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase

import json

class CreateGameTest(APITestCase):

    def test_create_game(self):
        response = self.client.post('/game/')
        self.assertEqual(200, response.status_code)

    def test_list_games(self):
        # Send a get request
        response = self.client.get('/game/')
        self.assertEqual(200, response.status_code)

        # Check game has a code
        result = json.loads(response.content.decode('utf-8'))
        self.assertNotEqual(len(result), 0)
        self.assertIsNotNone(result.code)
