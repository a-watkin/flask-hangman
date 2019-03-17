# Python standard library
import os
import subprocess

# Flask
from flask import Flask, render_template

# SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy


# Import blueprints routes here


app = Flask(__name__)
# Apply config values
app.config.from_object('config.DevelopmentConfig')

# Add database connection
db = SQLAlchemy(app)


def init_db():
    """
    Prevent auto linters from moving import to the top of the module.
    """
    # import models here


init_db()

# Register routes here

# Home page
@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')
