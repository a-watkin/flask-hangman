from app import db
from flask_sqlalchemy import SQLAlchemy


class HighScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
player = HighScores(username="test", score=10)
print(player.username, player.score)
db.session.add(player)
db.session.commit()
