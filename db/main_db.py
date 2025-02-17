# main_db.py
import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite')
cursor = db.cursor()

async def create_tables():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_registered)


async def create_tables_store():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_store)


async def create_tables_products_details():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_products_details)


async def sql_insert_registered(fullname, age, gender, date_age, email, photo):
    cursor.execute(queries.INSERT_TABLE_registered, (fullname, age, gender, date_age, email, photo))
    db.commit()



async def sql_insert_store(name_product, size, price, photo, productid):
    cursor.execute(queries.INSERT_TABLE_store, (name_product, size, price, photo, productid))
    db.commit()


async def sql_insert_products_details(productid, category, infoproduct):
    cursor.execute(queries.INSERT_TABLE_products_details, (productid, category, infoproduct))
    db.commit()