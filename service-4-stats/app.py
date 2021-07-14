from flask import Flask
from random import randint, randrange

app = Flask(__name__)

# generate stats 
@app.route('/get_stats', methods=['POST', 'GET'])
def get_stats():
    attack = 0
    intelligence = 0
    dexteriy = 0
    class == requests.get('htp://class_api:5000/get_class', data=class.text)
    if class == "Warrior":
        attack += randint(1, 2) + randint(1, 2) + 2
        intelligence += randint(1, 2) + randint(1, 2) 
        dexteriy += randint(1, 2) + randint(1, 2) 
        stats = ("Attack: " + str(attack)) + ("Intelligence:" + str(intelligence)) + ("Dexterity:" + str(dexterity)) 
        return stats

    elif class == "Mage":
        attack += randint(1, 2) + randint(1, 2)  
        intelligence += randint(1, 2) + randint(1, 2) + 2
        dexteriy += randint(1, 2) + randint(1, 2)
        stats = ("Attack: " + str(attack)) + ("Intelligence:" + str(intelligence)) + ("Dexterity:" + str(dexterity)) 
        return stats

    elif class == "Ranger":
        attack += randint(1, 2) + randint(1, 2)  
        intelligence += randint(1, 2) + randint(1, 2) 
        dexteriy += randint(1, 2) + randint(1, 2) + 2
        stats = ("Attack: " + str(attack)) + ("Intelligence:" + str(intelligence)) + ("Dexterity:" + str(dexterity)) 
        return stats
    

# generate points 
@app.route('/get_points', methods=['POST'])
def get_points():
    points = randint(4, 5, 6)
    return points

if __name__ == "__main__":
    app.run(port=5003, debug=True)