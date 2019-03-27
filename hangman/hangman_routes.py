import json
from flask import Blueprint, request, render_template

from .hangman import Hangman
from .hangman_model import db, HighScores

hangman_blueprint = Blueprint('hangman', __name__)


@hangman_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """
    Loads the page and gets the high scores.
    """

    high_scores = HighScores.query.order_by(
        HighScores.score.desc()).limit(10).all()

    if request.method == 'POST':
        username = request.form.get('username' or 'player-one')
        score = request.form.get('score')

        if score is None:
            score = 0

        player = HighScores(username=username, score=score)
        db.session.add(player)
        db.session.commit()

        high_scores = HighScores.query.order_by(
            HighScores.score.desc()).limit(10).all()

    return render_template('hangman/index.html', scores=high_scores)


@hangman_blueprint.route('/guess-word', methods=['GET'])
def get_guess_word():
    """
    Sends JSON data to start the game.
    """
    h = Hangman()
    return json.dumps(h.get_class_as_dict())


@hangman_blueprint.route('/check-guess', methods=['POST'])
def check_guess():
    """
    Receives and checks JSON data.
    """
    args = request.get_json()
    h = Hangman(args)

    if "current_guess" in args:
        guess = ''.join(args["current_guess"])

        if len(guess) == len(h.display_word):
            h.check_current_guess(guess)

        else:
            for char in guess:
                if char in h.display_word:
                    pass
                # Only allows one char to be guessed.
                elif len(set(guess) - set(h.display_word)) == 1:
                    h.check_current_guess(char)

    return json.dumps(h.get_class_as_dict())
