import os
import sqlite3 as sq

__DB = None


def reset_db(dbfile):
    """delete db if not already open"""
    try:
        os.remove(dbfile)
    except PermissionError:
        pass


def get_connection(dbfile):
    """connect to db file or create it"""
    global __DB

    if not __DB:
        print('creating connection...')
        __DB = sq.connect(dbfile)
    else:
        print('connection already existing')
    return __DB


def table_exists(db, table):
    """checks if table exists"""
    sql = f"SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{table}'"
    cursor = db.cursor()
    print(f'checking if {table!r} exists...')
    result = cursor.execute(sql).fetchall()
    return result


def create_table(db, filename=None, sql=None):
    """create table events from external file if it doesnt exists"""

    if filename:
        with open(filename) as sqlfile:
            sql = sqlfile.read()

    cursor = db.cursor()
    print('creating table...')
    cursor.execute(sql).connection.commit()


if __name__ == '__main__':
    db = get_connection('data.db')
    if not table_exists(db, 'events'):
        create_table(db, filename='events.sql')
    db2 = get_connection('data.db')
    print(db2 is db)
