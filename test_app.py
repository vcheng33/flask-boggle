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
            self.assertIn(data["gameId"],games)
            
            # write a test for this route
    
    def test_api_score_word(self):
        """Test scoring a new word"""

        with self.client as client:
            # with client.session_transaction() as change_session:
            response = client.post("/api/new-game")
            # response_score_words = client.post("/api/score-words")

            data = response.get_json()

            game_id = data["gameId"]
            response_from_score_words = {"gameId":game_id,"wordInput":"HELLO"}
            games[game_id].board = [['R', 'S', 'W', 'E', 'A'],
                                    ['N', 'O', 'O', 'O', 'E'],
                                    ['L', 'F', 'A', 'A', 'D'],
                                    ['X', 'K', 'M', 'T', 'E'],
                                    ['P', 'L', 'R', 'T', 'Y']]

            # If word is not in the word_list, it should return a json saying {result: "not-word"}
            self.assertEqual(score_word())
            # If word is in the word_list but not on the board, it should return a json saying '{result: "not-on-board"}' 
            # If word is in word_list and on the board, it should return a json saying '{result: "ok"}'



            self.assertIsInstance(data["wordInput"], str)


