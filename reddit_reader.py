from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app, "/reddit_reader")


def get_headlines():
    user_pass_dict = {'user': 'USERNAME',  # enter username
                      'password': 'PASSWORD',  # enter password
                      'api_type': 'json'}
    sess = requests.session()
    sess.headers.update({'User-Agent': 'Alexa Request'})
    sess.post('http://reddit.com/api/login', data=user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/ubiquiti/.json?limit=10'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = '... '.join(i for i in [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']])
    return titles


@app.route('/')
def homepage():
    return "homepage"


@ask.launch
def start_skill():
    welcome_message = 'Hello, Welcome to reddit reader, would you like the reddit headlines?'
    return question(welcome_message)


@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'the current world news headlines are {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("NoIntent")
def no_intent():
    return statement("Okay... bye")

if __name__ == '__main__':
    app.run()

titles = get_headlines()
print(titles)