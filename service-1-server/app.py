from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import os

app = Flask(__name__)

print('= config ==============================================')

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['SECRET_KEY'] = getenv('SKEY')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

print('= routes ==============================================')

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race = db.Column(db.String(10))
    character_class = db.Column(db.String(10))
    blessing = db.Column(db.String(50))
    stats = db.Column(db.String(200))
    points = db.Column(db.Integer)

# home route here
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    race = requests.get('http://race_api:5001/get_race') # container name needs to match http link
    character_class = requests.get('http://class_api:5002/get_class')
    blessing = requests.post('http://stats_api:5003/get_blessing', data=character_class.text)
    stats = requests.post('http://stats_api:5003/get_stats', data=character_class.text)
    points = requests.get('http://stats_api:5003/get_points')
    
    last_five_characters =okay try running docker-compose --version Character.query.order_by(Character.id.desc()).limit(10).all()
    db.session.add(
        Character(
            race=race.text,
            character_class=character_class.text,
            blessing=blessing.text,
            stats=stats.text,
            points=points.text
        )
    )
    db.session.commit()
    
    return render_template('index.html', race=race.text, character_class=character_class.text, blessing=blessing.text, stats=stats.text, points=points.text, last_five_characters=last_five_characters)

print('= home ==============================================')

# end 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    