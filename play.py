'''
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random": "true"}

headers = {
	"X-RapidAPI-Key": os.getenv('X-RAPIDAPI-KEY'),
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

res = requests.request("GET", url, headers=headers, params=querystring)

#print(res.json()['word'])
'''

class State:

    def __init__(self):
        self.word = 'hangman'
        self.board = ['_' for l in self.word]

    def play(self, guess):
        self.guess = guess

        for i, l in enumerate(self.word):
            if guess == l:
                self.board[i] = [*self.word][i]

from flask import Flask, request

app = Flask(__name__)
s = State()

@app.route('/', methods=['GET', 'POST'])
def index():
    g = request.args.get('guess')
    s.play(guess=g)
    if s.board == [*s.word]:
        s.board = f"You guessed it! The word is {s.word}."
    r = open('index.html').read()
    return r.replace('start', ' '.join(s.board) if type(s.board) != str else s.board)

if __name__ == '__main__':
    app.run(debug=True)

