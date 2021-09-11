from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4

from boggle import BoggleGame
# from wordlist import english_words
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"
debug = DebugToolbarExtension(app)

# The boggle games created, keyed by game id
games = {}
GAME_ID_KEY = "game_id_key"

@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    breakpoint()

    #session[GAME_ID_KEY] = game_id

    return {"gameId": game_id, "board": game.board}

@app.post("/api/score-word")
def score_word():
    """Listen for a POST request, expect a jSON with game_id and word"""
    #game_id = session[GAME_ID_KEY]

    word = request.json.get("wordInput")
    game_id = request.json.get("gameId")
    breakpoint()
    game = games[game_id]

    if game.is_word_in_word_list(word) is not True:
        # result = jsonify('{result: "not-word"}')
        breakpoint()
        return jsonify('{result: "not-word"}')
        # return result
    elif game.check_word_on_board(word) is not True:
        # result = jsonify('{result: "not-on-board"}')
        breakpoint()
        # return result
        return jsonify('{result: "not-on-board"}')
    else:
        # result = jsonify('{result: "ok"}')
        breakpoint()
        # return result
        return jsonify('{result: "ok"}')

    # input_word = response[""]
    #breakpoint()
    #wordInput
    # We need to get the word that was provided
    # We need to run the methods is_word_in_word_list(word) and check_word_on_board(word)

"""Make a new route with a path of /api/score-word. This is an API route — it’s going to be called via AJAX in the browser, not from normal browser form submissions!

This should accept a POST request with JSON for the game id and the word. It should check if the word is legal:

It should be in the word list
It sound be findable on the board
This route should return a JSON response using Flask’s jsonify function.

if not a word: {result: "not-word"}
if not on board: {result: "not-on-board"}
if a valid word: {result: "ok"}"""
