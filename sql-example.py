import os
import sqlite3 as sq

DBFILE = 'sql-examples.db'
#
# delete db if not already open
#
try:
    os.remove(DBFILE)
except PermissionError:
    pass
#
# connect to db file or create it
#
connection = sq.connect(DBFILE)
#
# get cursor from connection
#
cursor = connection.cursor()
#
# create table events if it doesnt exists
#
sql_create_events_table = """
CREATE TABLE IF NOT EXISTS events (
    band text,
    city text,
    date text
); 
"""
cursor.execute(sql_create_events_table).connection.commit()
#
# delete all records created by this script
#
cursor.execute("""
    DELETE FROM events WHERE band='a' or band like 'band%'
""").connection.commit()
#
# insert single record, pure SQL
#
cursor.execute("""
    INSERT INTO events VALUES ('a', 'b', 'c')
""").connection.commit()
#
# insert single record, SQL and python
#
rows = []
rows.append(('bandname', 'bandcity', 'banddate'))
cursor.execute(
    'INSERT INTO events VALUES (?, ?, ?)',
    rows[0]
).connection.commit()
#
# insert multiple records, SQL and python
#
rows = []
rows.append(('bandname', 'bandcity', 'banddate'))
rows.append(('bandname2', 'bandcity2', 'banddate2'))
cursor.executemany(
    'INSERT INTO events VALUES (?, ?, ?)',
    rows
).connection.commit()
#
# select all from events
#
rows = cursor.execute("""
    SELECT * FROM events
""").fetchall()
print(rows)

