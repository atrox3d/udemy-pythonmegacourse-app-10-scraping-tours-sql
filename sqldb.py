import sqlite_helper as sqle

DBFILE = 'data.db'
TABLE = 'events'
SQLFILE = 'events.sql'


def get_connection():
    db = sqle.get_connection(DBFILE)
    return db


def read():
    db = get_connection()
    cursor = db.cursor()
    sql = f'SELECT * from {TABLE}'
    cursor.execute(sql)
    return cursor.fetchall()


def store(fields):
    db = get_connection()
    cursor = db.cursor()
    sql = f'INSERT INTO {TABLE} VALUES(?, ?, ?)'
    cursor.execute(sql, fields)
    db.commit()


db = get_connection()
if not sqle.table_exists(db, TABLE):
    sqle.create_table(db, filename=SQLFILE)

if __name__ == '__main__':
    db1 = get_connection()
    db2 = get_connection()
    print(db1 is db2)
    print(read())


