#hangman
---
hangman is a [weird game](https://youtu.be/le5uGqHKll8).

usage
---
this uses WordsAPI so first get RapidAPI key and make `.env` file
```
vim .env
#then...
X-RAPIDAPI-KEY= #your RapidAPI key
```

i use Flask so webserver runs on localhost:5000
```
pipenv run python3 play.py
```

todo
---
* auto draw hangman when wrong
* allow wordlist
* add letter tracker
* make pretty

