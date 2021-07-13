from flask import Flask
import random

app = Flask(__name__)

# Generate Charecters class
@app.route('/')
def get_class():
    return random.choice(["Warrior", "Mage", "Ranger"])

# generate blessing 
@app.route('/')
def get_blessing():
    blesing = {
        "Warrior" = 'Recieve the blessing of Ares - God of war: +2 Attack'
        "Mage" = 'Recieve the blessing of Athena - God of wisdom: +2 Intellect'
        "Ranger" = 'Recieve the blessing of Artemis - God of the hunt: +2 Dexterity'
    }
    return blessing[request.data.decode("utf.8")]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)