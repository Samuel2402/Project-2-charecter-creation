from flask import Flask, render_template
import requests

app = Flask(__name__)

# home route here
@app.route('/')
@app.route('/home')
def home():
    race = requests.post('http://character_api:5000/get_race', data=race.text) # container name needs to match http link
    class = requests.post('http://character_api:5000/get_class', data=class.text)
    blessing = requests.post('http://character_api:5000/get_blessing', data=blessing.text)
    stats = requests.post('http://character_api:5000/get_stats', data=stats.text)
    points = requests.post('http://character_api:5000/get_points', data=points.text)
    return render_template('index.html', race=race.txt, class=class.txt, blessing=blessing.txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    