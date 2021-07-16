

# home route here
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    race = requests.get('http://race_api:5001/get_race') # container name needs to match http link
    character_class = requests.get('http://class_api:5002/get_class')
    blessing = requests.post('http://class_api:5002/get_blessing', data=blessing.text)
    stats = requests.post('http://stats_api:5003/get_stats', data=character_class.text)
    points = requests.get('http://stats_api:5003/get_points')
    character = Character(
        race=race.text,
        character_class=character_class.text,
        blessing=blessing.text,
        stats=stats.text,
        points=points.text
        )
    db.session.add(character)
    db.session.commit()
    return render_template('index.html', race=race.txt, character_class=character_class.txt, blessing=blessing.txt, stats=stats.txt, points=points.txt)

print('= home ==============================================')