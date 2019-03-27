from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HighScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
