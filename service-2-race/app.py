from flask import Flask
import random

app = Flask(__name__)

# Generate Characters race
@app.route('/get_race', methods=['GET'])
def get_race():
    return random.choice(["Human", "Elf", "Orc"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)