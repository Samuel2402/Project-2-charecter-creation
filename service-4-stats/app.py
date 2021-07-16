from flask import Flask, request
from random import randint, randrange
import requests

app = Flask(__name__)

# generate blessing 
@app.route('/get_blessing', methods=['POST'])
def get_blessing():   
    character_class = request.data.decode('utf-8')
    blessing = ""

    if character_class == "Warrior":
        blessing += 'Recieve the blessing of Ares: +2 base Attack'
        return blessing

    if character_class == "Mage":
        blessing += 'Recieve the blessing of Athena: +2 base Intellect'
        return blessing

    if character_class == "Ranger":
        blessing += 'Recieve the blessing of Artemis: +2 base Dexterity'
        return blessing

# generate stats 
@app.route('/get_stats', methods=['POST'])
def get_stats():
    attack = 0
    intelligence = 0
    dexterity = 0
    character_class = request.data.decode('utf-8')
    
    if character_class == "Warrior":
        attack += randint(1, 2) + randint(1, 2) + 2
        intelligence += randint(1, 2) + randint(1, 2) 
        dexterity += randint(1, 2) + randint(1, 2) 
        stats = "Attack: " + str(attack) + " | " + "Intelligence:" + str(intelligence) + " | " + "Dexterity:" + str(dexterity)    # "Attack: 0  |  Intelligence: 0  |  Dexterity: 0" 
        return stats

    elif character_class == "Mage":
        attack += randint(1, 2) + randint(1, 2)  
        intelligence += randint(1, 2) + randint(1, 2) + 2
        dexterity += randint(1, 2) + randint(1, 2)
        stats = "Attack: " + str(attack) + " | " + "Intelligence:" + str(intelligence) + " | " + "Dexterity:" + str(dexterity) 
        return stats

    elif character_class == "Ranger":
        attack += randint(1, 2) + randint(1, 2)  
        intelligence += randint(1, 2) + randint(1, 2) 
        dexterity += randint(1, 2) + randint(1, 2) + 2
        stats = "Attack: " + str(attack) + " | " + "Intelligence:" + str(intelligence) + " | " + "Dexterity:" + str(dexterity) 
        return stats
    
    else:
        return "error no input generated"

# generate points 
@app.route('/get_points', methods=['GET'])
def get_points():
    points = randint(4, 6)
    return str(points)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)