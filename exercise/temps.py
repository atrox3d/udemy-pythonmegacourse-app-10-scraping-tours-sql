import datetime as dt
import requests
import selectorlib
import json


URL = 'https://programmer100.pythonanywhere.com'


def get_headers(filename='headers.txt'):
    with open(filename) as file:
        _, dictionary = file.read().split('=')
        headers = json.loads(dictionary)
        return headers


def scrape(url, headers=None):
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


def timestamp():
    return dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


def header():
    return 'date,temperature'


def store(date, temp, filename='temps.csv'):
    try:
        with open(filename) as test:
            test.readline()
    except FileNotFoundError:
        with open(filename, 'w') as head:
            head.write(f'{header()}\n')

    with open(filename, 'a') as out:
        line = f'{date},{temp}\n'
        out.write(line)


def update():
    scraped = scrape(URL, get_headers('../headers.txt'))
    temp = extract(scraped)
    now = timestamp()
    store(date=now, temp=temp)


if __name__ == '__main__':
    update()
