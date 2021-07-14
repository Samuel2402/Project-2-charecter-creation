from app.py import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race = db.Column(db.String(10))
    character_class = db.Column(db.String(10))
    blessing = db.Column(db.String(50)
    stats = db.String(db.String(100))
    points = db.Column(db.Integer(1))
