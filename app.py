import io
import codecs

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test application Flashcards!!!"

@app.route("/GetRiim/<int:entityId>")
def get_riim(entityId):
    inputfile = "./resources/1.png"
    f=codecs.open(inputfile, 'r')
    image = f.read()
    response = Flask.make_response(image)
    response.headers.set('Content-Type', 'image/png')
    #response.headers.set('Content-Disposition', 'attachment', filename='%s.jpg' % pid)
    response.headers.set('Content-Disposition', 'attachment', filename=inputfile)
    #return "Entity Value:" + str(entityId)
    return response
