from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey,it's lancer's modification!"
