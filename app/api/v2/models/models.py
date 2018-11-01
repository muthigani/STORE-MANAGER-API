
from flask import jsonify
from db_conn import conn
from datetime import datetime



class Products:
    def __init__(self, productname, quantity, price):
        self.productname = productname
        self.quantity = quantity
        self.price = price
        self.date = datetime.now().__str__()



    def savedata(self):

        #connect = connection()
        curr = conn.cursor()

        product = """INSERT INTO
                products  (productname,quantity,price,date)
                VALUES ('%s','%s','%s','%s')"""\
                 % (self.productname, self.quantity, self.price, self.date)
        curr.execute(product)
        conn.commit()
        return jsonify({'message': 'Product successfully created '})

    def serializer(self):

        return dict(
            productname=self.productname,
            quantity=self.quantity,
            price=self.price,
            date=self.date
        )

class UserModel:
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.date = datetime.now().__str__()



    def saveuser(self):

        #connect = connection()
        curr = conn.cursor()

        users = """INSERT INTO
                users  (username,email,password,role,date)
                VALUES ('%s','%s','%s','%s','%s')"""\
                 % (self.username, self.email, self.password,self.role,self.date)
        curr.execute(users)
        conn.commit()

        return jsonify({'message': 'Product successfully created '})

    def serializer(self):

        return dict(
            username=self.username,
            email=self.email,
            password=self.password,
            role=self.role,
            date=self.date
        )

class Sales:
    def __init__(self, product, quantity, sold_by, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.sold_by = sold_by
        self.date = datetime.now().__str__()



    def savedata(self):

        #connect = connection()
        curr = conn.cursor()

        sales = """INSERT INTO
                sales  (product,quantity,sold_by,price,date)
                VALUES ('%s','%s','%s','%s','%s')"""\
                 % (self.product, self.quantity, self.price, self.sold_by, self.date)
        curr.execute(sales)
        conn.commit()
        return jsonify({'message': 'Sales successfully created '})

    def serializer(self):

        return dict(
            productname=self.product,
            quantity=self.quantity,
            price=self.price,
            sold_by=self.sold_by,
            date=self.date
        )