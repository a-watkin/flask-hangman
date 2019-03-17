from flask import Blueprint, request, render_template

hangman_blueprint = Blueprint('hangman', __name__)


@hangman_blueprint.route('/', methods=['GET'])
def index():
    return render_template('hangman/index.html')
