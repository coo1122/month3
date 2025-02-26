# queries.py

TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    gender TEXT,
    date_age TEXT,
    email TEXT,
    photo TEXT
    )
"""


INSERT_TABLE_registered = """
    INSERT INTO registered (fullname, age, gender, date_age, email, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""


TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    productid TEXT
    )
"""


INSERT_TABLE_store = """
    INSERT INTO store (name_product, size, price, photo, productid)
    VALUES (?, ?, ?, ?, ?)
"""


TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    infoproduct TEXT
    )
"""


INSERT_TABLE_products_details = """
    INSERT INTO products_details (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""


TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
    )
"""


INSERT_TABLE_collection_products = """
    INSERT INTO collection_products (productid, collection)
    VALUES (?, ?)
"""