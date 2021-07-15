import io
import codecs

from flask import Flask, send_file
from random import seed
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test application Flashcards!!!"

@app.route("/GetRiim/<int:entityId>")
def get_riim(entityId):
    seed(entityId)
    riim = randint(1,5)

    inputfile = "./resources/%s.png" % str(riim)
    image = bytearray()    
    f=open(inputfile, 'rb')
    
    byte = f.read(1)    
    while byte:
        image.append(byte[0])
        byte =f.read(1)
   
    f.close()
    #response = Flask.make_response(image)
    #response.headers.set('Content-Type', 'image/png')
    #response.headers.set('Content-Disposition', 'attachment', filename='%s.jpg' % pid)
    #response.headers.set('Content-Disposition', 'attachment', filename=inputfile)
    #return "Entity Value:" + str(entityId)    
    return send_file(io.BytesIO(image) ,attachment_filename='logo.png',mimetype='image/png')
