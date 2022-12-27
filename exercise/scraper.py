import requests
import selectorlib
import json


def get_headers(filename='headers.txt'):
    with open(filename) as file:
        _, dictionary = file.read().split('=')
        headers = json.loads(dictionary)
        return headers


def scrape(url, headers=get_headers('../headers.txt')):
    response = requests.get(url, headers=headers)
    source = response.text
    return source


def extract(source):
    key = 'temp'
    yaml = f"""
        {key}:
            css: '#temperatureId'
    """
    extractor = selectorlib.Extractor.from_yaml_string(yaml)
    extracted = extractor.extract(source)[key]
    return extracted
