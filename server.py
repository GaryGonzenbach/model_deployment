from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/ada')
def ada_page():
   return 'The ada cohort is my favorite data science class'  

@app.route('/roll-dice')
def dice_page():
   randomdice = randint(1,7)
   return ('roll the dice: '+str(randomdice))