from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")


def get_headlines():
    pass

@app.route('/')

if __name__ = '__main__':
    app.run()