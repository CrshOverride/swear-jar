import os
from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/word')
def generate_word():
    return "Hello World!"
