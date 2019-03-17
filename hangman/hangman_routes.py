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
    if 'current_guess' in args:
        guess = ''.join(args['current_guess'])
        h.check_current_guess(guess)
        print('yes')

    return json.dumps(h.get_class_as_dict())
