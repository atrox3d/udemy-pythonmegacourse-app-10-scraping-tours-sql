import sqlite3 as sq


def get_connection(filename='temps.db'):
    db = sq.connect(filename)
    return db


def create_table(db, filename=None, sql=None):
    with open('temps.sql') as sqlfile:
        sql = sqlfile.read()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


def store(date, temp, db=get_connection()):
    sql = 'INSERT INTO temps VALUES(?, ?)'
    cursor = db.cursor()
    cursor.execute(sql, (date, temp))
    db.commit()


def merge(db, csv_path):
    cursor = db.cursor()

    with open(csv_path) as csv_in:
        content = csv_in.read()
        lines = [line for line in content.split('\n') if line]
        sql = 'SELECT * from temps WHERE date=? AND temperature=?'
    for line in lines[1:]:
        print(f'{line=}')
        date, temp = line.split(',')
        cursor.execute(sql, (date, temp))
        if not cursor.fetchall():
            store(date, temp)


db = get_connection()
create_table(db, 'temps.sql')

if __name__ == '__main__':
    db = get_connection()
    create_table(db, 'temps.sql')
    merge(db, 'temps.csv')
