from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['SECRET_KEY'] = getenv('SKEY')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
app = Flask(__name__)

# home route here
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    race = requests.get('http://race_ipa:5001/get_race', data=race.text) # container name needs to match http link
    character_class = requests.get('http://class_api:5002/get_class', data=class.text)
    blessing = requests.get('http://class_api:5002/get_blessing', data=blessing.text)
    stats = requests.get('http://stats_api:5003/get_stats', data=stats.text)
    points = requests.get('http://stats_api:5003/get_points', data=points.text)
    return render_template('index.html', race=race.txt, class=class.txt, blessing=blessing.txt, stats=stats.txt, points=points.txt)
    def character():
        return character = Character(race=race.text, class=class.text, blessing=blessing.text, stats=stats.text, points=points.text)
        db.session.add(character)
        db.session.commit()

# add to db
# db.session.add(character)
# db.session.commit()

# add view previous 

# end 
if __name__ == "__main__":
    app.run(port=5000, debug=True)

    