from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test application Flashcards!!!"

@app.route("/GetRiim/<int:entityId>")
def get_riim(entityId):
    return "Entity Value:" + str(entityId)
