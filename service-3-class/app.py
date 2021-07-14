from flask import Flask
import random

app = Flask(__name__)

# Generate Charecters class
@app.route('/get_class', methods=['POST'])
def get_class():
    return random.choice(["Warrior", "Mage", "Ranger"])

# generate blessing 
@app.route('/get_blessing', methods=['POST'])
def get_blessing():   # can use if statements IF needed
    blesing = {         
        "Warrior" == 'Recieve the blessing of Ares - God of war: +2 base Attack'
        "Mage" == 'Recieve the blessing of Athena - God of wisdom: +2 base Intellect'
        "Ranger" == 'Recieve the blessing of Artemis - God of the hunt: +2 base Dexterity'
    }
    return blessing[request.data.decode("utf.8")]

if __name__ == "__main__":
    app.run(port=5002, debug=True)