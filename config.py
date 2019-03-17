import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'database.db')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # You have to set development before the app runs as an env variable
    # export FLASK_ENV=development
    pass
