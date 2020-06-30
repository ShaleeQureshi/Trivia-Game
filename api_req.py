import requests
import json

source = requests.get("https://opentdb.com/api.php?amount=1&category=19&difficulty=medium&type=boolean")
data = source.json()

def getQuestion():
    return (data['results'][0]['question'])

def getAnswer():
    return (data['results'][0]['correct_answer'])
