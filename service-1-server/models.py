print('= Import-for-table ==============================================')

from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race = db.Column(db.String(10))
    character_class = db.Column(db.String(10))
    blessing = db.Column(db.String(50))
    stats = db.Column(db.String(100))
    points = db.Column(db.Integer)

print('= end-table ==============================================')
