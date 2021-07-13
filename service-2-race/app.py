from flask import Flask
import random

app = Flask(__name__)

# Generate Charecters race
@app.route('/')
def get_race():
    return random.choice(["Human", "Elf", "Orc"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)