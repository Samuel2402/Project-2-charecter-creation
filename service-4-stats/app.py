from flask import Flask
import random

app = Flask(__name__)

# generate stats 
@app.route('/')
def get_stats():
    attack = 0
    intelligence = 0
    dexteriy = 0
    class = requests.get('htp://class_api:5000/get_class', data=class.text)
    if class = "warrior":
        attack += 5
        intelligence += 3
        dexteriy += 3
        stats = {
            "attack" = str(attack)
            "intelligence" = str(intelligence)
            "dexterity" = str(dexterity) 
            }       
        return stats

    elif class = "mage":
        attack += 3
        intelligence += 5
        dexteriy += 3
        stats = {
            "attack" = str(attack)
            "intelligence" = str(intelligence)
            "dexterity" = str(dexterity) 
            }
        return stats

    elif class = "ranger":
        attack += 3
        intelligence += 3
        dexteriy += 5
        stats = {
            "attack" = str(attack)
            "intelligence" = str(intelligence)
            "dexterity" = str(dexterity) 
        }
        return stats
    

# generate points 
@app.route('/')
def get_points():
    points = randint[4,5,6]
    return points

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)