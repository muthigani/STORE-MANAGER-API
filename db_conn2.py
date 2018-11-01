import psycopg2
from flask import Flask, Blueprint

#url = "dbname='storemanager' host='127.0.0.1' port='5432' user='postgres' password='admin'"

def connection():
    con = psycopg2.connect("dbname='storemanager' host='127.0.0.1' port='5432' user='postgres' password='admin'")
    return con


def create_tables():
    conn = connection()
    curr = conn.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)
    conn.commit()

def destroy_tables():
    pass

def tables():
    users = '''CREATE TABLE IF NOT EXISTS users (
    userid serial PRIMARY KEY,
    fullname varchar (50)NOT NULL,
    username varchar (50)NOT NULL,
    email varchar (100)NOT NULL,
    password varchar (50)NOT NULL,
    role varchar (50) NOT NULL,
    date timestamp 
    )'''
    products = '''CREATE TABLE IF NOT EXISTS products (
    productid serial PRIMARY KEY,
    fullname varchar (50)NOT NULL,
    quantity varchar (50)NOT NULL,
    price varchar (50)NOT NULL,
    date timestamp
    )'''

    queries = [users, products]

    return queries