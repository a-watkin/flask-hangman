import json
from flask import Blueprint, request, render_template

from .hangman import Hangman

hangman_blueprint = Blueprint('hangman', __name__)


@hangman_blueprint.route('/', methods=['GET'])
def index():
    return render_template('hangman/index.html')


@hangman_blueprint.route('/guess-word', methods=['GET'])
def get_guess_word():
    h = Hangman()
    return json.dumps(h.get_class_as_dict())


@hangman_blueprint.route('/check-guess', methods=['POST'])
def check_guess():
    args = request.get_json()
    h = Hangman(args)

    # if guess in
    if "current_guess" in args:
        guess = ''.join(args["current_guess"])

        # if guess is as long as the hidden word
        if len(guess) == len(h.display_word):
            h.check_current_guess(guess)

        else:
            # this part kind of sucks but i'm running out of time
            for char in guess:
                # only allows one char to be guessed at a time
                if char in h.display_word:
                    pass
                elif len(set(guess) - set(h.display_word)) == 1:
                    h.check_current_guess(char)

        if h.game_won:
            print('write to database')

    return json.dumps(h.get_class_as_dict())
