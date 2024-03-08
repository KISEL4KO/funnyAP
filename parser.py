import requests
from bs4 import BeautifulSoup


def request(number):
    res = requests.get(f'http://numbersapi.com/{number}/trivia')
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


print(request('1'))