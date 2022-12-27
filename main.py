import time

from mailer import send_mail
import scraper
import textdb
import sqldb

URL = 'https://programmer100.pythonanywhere.com/tours/'

db = textdb
db = sqldb
SECONDS = 0
while True:
    scraped = scraper.scrape(URL)
    extracted = scraper.extract(scraped)
    print(f'{extracted=}')
    if extracted != 'No upcoming tours':
        fields = [item.strip() for item in extracted.split(',')]
        content = db.read()
        if tuple(fields) not in content:
            db.store(fields)
            send_mail(subject='Hey, new event was found', body=f'{extracted}')
        else:
            print('event already sent')

    if SECONDS:
        time.sleep(SECONDS)
    else:
        break
