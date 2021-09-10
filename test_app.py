from unittest import TestCase

from flask import json

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # Not specifically requested but adding for practice for ourselves
            self.assertEqual(response.status_code, 200)
            self.assertIn('<form id="newWordForm">', html)
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.post('/api/new-game')
            
            data = response.get_json()
            # text = response.get_data(as_text=True)
            # breakpoint()
            self.assertIsInstance(data["gameId"], str)
            self.assertIsInstance(data["board"], list)
            self.assertEqual(len(games), 1)
            
            # write a test for this route
