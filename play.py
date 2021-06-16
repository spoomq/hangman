import os
from os.path import join, dirname
import sys
import json
import requests
from dotenv import load_dotenv
import jyserver.Flask as jsf
from flask import Flask, Response, request, render_template, url_for

PATH = join(dirname(__file__), '.env')
load_dotenv(PATH)
url = 'https://wordsapiv1.p.rapidapi.com/words/'
query = {'random': 'true'}
headers = {
        'x-rapidapi-key': os.environ.get('X-RAPIDAPI-KEY'),
        'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com'
        }
api = requests.request('GET', url, headers=headers, params=query)
response = json.loads(api.text)

#response = 'weird'

app = Flask(__name__)

@jsf.use(app)
class State:
    word = [l for l in response['word'][:2] + response['word'][2:]]
    try: 
        hint = response['results'][0]['definition']
    except KeyError:
        hint = 'This word has no definition, good luck!'

    #word = [l for l in response[:2] + response[2:]]
    #hint = 'an adjective for hangman'

    def __init__(self):
        self.board = ['_' for i in range(0, len(self.word))]
        for i in range(0, len(self.word)):
            if self.word[i] == ' ':
                self.board[i] = ' '

    def push(self, guess=None):
        if guess != None:
            for i in range(0, len(self.word)):
                if guess == self.word[i]:
                    self.board[i] = guess
        else:
            self.guess = guess

    @jsf.task
    def play(self):
        while self.board != self.word:
            self.js.dom.board.innerHTML = ' '.join(map(str, self.board))
            self.js.dom.hint.innerHTML = self.hint
        else:
            self.js.dom.win.innerHTML = 'You solved it!'


@app.route('/')
def index():
    State.play()
    return State.render(open('index.html').read())

if __name__ == '__main__':
    app.run(debug=True)
