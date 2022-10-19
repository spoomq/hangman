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

class State:

    def __init__(self):
        self.word = res.json()['word']
        self.board = ['_' for l in self.word]
        self.count = 0

    def play(self, guess: str):
        self.guess = guess
        index = []
        letter = []

        for i, l in enumerate(self.word):
            if guess == l:
                index.append(i)
                letter.append(l)

        if len(index) > 1:
            for i in range(len(index)):
                self.board[index[i]] = letter[i]
        elif len(letter) < 1:
            self.count += 1
        else:
            self.board[index[0]] = letter[0]
        index.clear()
        letter.clear()

from flask import Flask, request

app = Flask(__name__)
s = State()

@app.route('/', methods=['GET', 'POST'])
def index():
    g = request.args.get('guess')
    s.play(guess=g)
    if s.board == [*s.word]:
        s.board = f"You guessed it! The word is {s.word}."
    elif s.count == 7:
        s.board = "YoU LoSE!"
    r = open('index.html').read()
    return r.replace('start', ' '.join(s.board) if type(s.board) != str else s.board).replace('wrong', str(s.count))

if __name__ == '__main__':
    app.run(debug=True)

