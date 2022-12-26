import requests
import selectorlib
import json

URL = 'https://programmer100.pythonanywhere.com/tours/'


def get_headers(filename='headers.txt'):
    with open('headers.txt') as file:
        _, dictionary = file.read().split('=')
        headers = json.loads(dictionary)
        return headers


def scrape(url, headers=None):
    """scrape the page source from the url"""
    response = requests.get(url, headers=headers)
    source = response.text
    return source


if __name__ == '__main__':
    source = scrape(URL, get_headers())
    search = '<h1 align="right " id="displaytimer">'
    for line in source.split('\n'):
        if search in line:
            print(line)
