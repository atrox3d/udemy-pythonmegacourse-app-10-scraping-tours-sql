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


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)
    print(f'{value=}')
    tours = value['tours']
    return tours


if __name__ == '__main__':
    scraped = scrape(URL, get_headers())

    # check if present in html
    search = '<h1 align="right " id="displaytimer">'
    for line in scraped.split('\n'):
        if search in line:
            print(line)

    extracted = extract(scraped)
    print(f'{extracted=}')

