import datetime as dt
import sys

import scraper
import textdb
import sqldb

URL = 'https://programmer100.pythonanywhere.com'


def timestamp():
    return dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


def update():
    scraped = scraper.scrape(URL)
    temp = scraper.extract(scraped)
    now = timestamp()
    textdb.store(date=now, temp=temp)
    sqldb.store(date=now, temp=temp)


if __name__ == '__main__':
    update()
