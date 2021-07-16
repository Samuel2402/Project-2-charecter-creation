from flask import Flask 
import random
import requests

app = Flask(__name__)

# Generate Characters class
@app.route('/get_class', methods=['GET'])
def get_class():
    return random.choice(["Warrior", "Mage", "Ranger"]) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)