from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "I wanna shoot out this fkin world"
