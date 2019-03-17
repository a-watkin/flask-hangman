import json
from flask import Blueprint, request, render_template

from .hangman import Hangman

hangman_blueprint = Blueprint('hangman', __name__)


@hangman_blueprint.route('/', methods=['GET'])
def index():
    return render_template('hangman/index.html')


@hangman_blueprint.route('/get/guess-word', methods=['GET'])
def get_guess_word():
    h = Hangman()
    return json.dumps(h.get_class_as_dict())
