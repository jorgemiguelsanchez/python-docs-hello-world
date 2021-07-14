from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/GetRiim/<int:entityId>")
def get_riim(entityId):
    return "Hello, World!" + entityId
