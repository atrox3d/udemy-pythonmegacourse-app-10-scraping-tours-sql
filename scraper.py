import json

import requests
import selectorlib


def get_headers(filename='headers.txt'):
    with open(filename) as file:
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
