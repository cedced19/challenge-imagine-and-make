from waitress import serve
from flask import Flask, render_template

app = Flask(__name__)

#import RPi.GPIO as GPIO
from threading import Thread
import time

@app.route('/')
def index():
    return render_template('index.html')

def commande1():
    time.sleep(5)
    print("Attente de 5s terminée")
    return True

@app.route('/ask/1')
async def ask1():
    print("Demande de 1")
    #on envoie la commande au robot de fournir l'objet 1
    thread = Thread(target=commande1, args=())
    thread.daemon = True
    thread.start()

    print("Réponse envoyé")
    return index()


serve(app, host='0.0.0.0', port=8000)