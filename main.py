import time

from mailer import send_mail
import scraper
import textdb

URL = 'https://programmer100.pythonanywhere.com/tours/'

SECONDS = 0
while True:
    scraped = scraper.scrape(URL)

    # check if present in html
    search = '<h1 align="right " id="displaytimer">'
    for line in scraped.split('\n'):
        if search in line:
            print(line)

    extracted = scraper.extract(scraped)
    print(f'{extracted=}')

    if extracted != 'No upcoming tours':
        try:
            content = textdb.read()
        except FileNotFoundError:
            content = []
        if extracted not in content:
            textdb.store(extracted)
            send_mail(subject='Hey, new event was found', body=f'{extracted}')
        else:
            print('event already sent')

    if SECONDS:
        time.sleep(SECONDS)
    else:
        break
