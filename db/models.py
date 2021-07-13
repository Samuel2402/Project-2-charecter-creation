from db import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race = db.Column(db.string(10))
    class = db.Column(db.String(10))
    blessing = db.Column(db.string(50)
    attack = db.Column(db.Integer(2))
    intelligence = db.Column(db.Integer(2))
    dexterity = db.Column(db.Integer(2))