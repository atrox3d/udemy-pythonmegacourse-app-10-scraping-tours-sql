import time

from mailer import send_mail
from scraper import get_headers, scrape, extract

URL = 'https://programmer100.pythonanywhere.com/tours/'


def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(f'{extracted}\n')


def read():
    with open('data.txt') as file:
        return file.read()


SECONDS = 0
while True:
    scraped = scrape(URL, get_headers())

    # check if present in html
    search = '<h1 align="right " id="displaytimer">'
    for line in scraped.split('\n'):
        if search in line:
            print(line)

    extracted = extract(scraped)
    print(f'{extracted=}')

    if extracted != 'No upcoming tours':
        try:
            content = read()
        except FileNotFoundError:
            content = []
        if extracted not in content:
            store(extracted)
            send_mail(subject='Hey, new event was found', body=f'{extracted}')
        else:
            print('event already sent')

    if SECONDS:
        time.sleep(SECONDS)
    else:
        break
