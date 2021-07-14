from flask import Flask
import random

app = Flask(__name__)

# Generate Charecters race
@app.route('/get_race', methods=['POST'])
def get_race():
    return random.choice(["Human", "Elf", "Orc"])


if __name__ == "__main__":
    app.run(port=5001, debug=True)