import psycopg2
import os

#db_url = os.getenv('DATABASE_URL')
#conn = psycopg2.connect(db_url)
conn = psycopg2.connect("dbname='storemanager' host='127.0.0.1' port='5432' user='postgres' password='admin'")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    userid serial PRIMARY KEY,
    username varchar (50)NOT NULL,
    email varchar (100)NOT NULL,
    password varchar (50)NOT NULL,
    role varchar (50) NOT NULL,
    date varchar
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS products (
    productid serial PRIMARY KEY,
    productname varchar (50)NOT NULL,
    quantity varchar (50)NOT NULL,
    price varchar (50)NOT NULL,
    date varchar
    )''')
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS sales (
    salesid serial PRIMARY KEY,
    product varchar (100)NOT NULL,
    quantity varchar (50)NOT NULL,
    price varchar (50)NOT NULL,
    sold_by varchar (50)NOT NULL,
    date varchar
    )''')
conn.commit()
