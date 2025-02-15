# main_db.py
import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite')
cursor = db.cursor()

async def create_tables():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_registered)


async def sql_insert_registered(fullname, age, gender, date_age, email, photo):
    cursor.execute(queries.INSERT_TABLE_registered, (fullname, age, gender, date_age, email, photo))
    db.commit()