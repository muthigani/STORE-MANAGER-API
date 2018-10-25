import os
from flask_restful import Resource, Api
from flask import jsonify, request, make_response
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token)

from app.api.v2.models.viewsmodel import *


class Signup(Resource):

    def post(self):
        #userid = request.get_json()['userid']
        name = request.get_json()['name']
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        role = request.get_json()['role']
        cur.execute("INSERT INTO users (name,username,email,password,role) VALUES('"+name+"','"+username+"','"+email+"','"+password+"','"+role+"');")
        conn.commit()

    def get(self):
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        if users is None:
            return jsonify ({'message': 'No users found'})
        else:
            return jsonify(users)
        conn.commit()

class Login(Resource):
    """login in registered users
        Returns:
            token and confirmation message
        """

    def post(self):
        email = request.get_json()["email"]
        password =request.get_json()["password"]

        if not email or not password:
            return jsonify({'message': 'email or password is missing'})

        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password,))
        users = cur.fetchone()
        access_token = create_access_token(identity=email)

        if users is not None:
            return jsonify(token=access_token, message="Login successful!")
        return jsonify({"message":"incorect Credentails"})
            #return jsonify(token=access_token, message="Login successful!")


        #return jsonify(token=access_token, message="Login successful!")

        conn.commit()


class ProductsList(Resource):
    @jwt_required
    def post(self):
        productname = request.get_json()['productname']
        quantity = request.get_json()['quantity']
        price = request.get_json()['price']
        cur.execute("INSERT INTO products (productname,quantity,price) VALUES('"+productname+"','"+quantity+"','"+price+"');")
        conn.commit()
        return jsonify({'message': 'Product successfully created '})

    @jwt_required
    def get(self):
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()

        if products is None:
            return jsonify ({'message' : 'No products found'})
        else:
            return jsonify(products)
        conn.commit()


class Product(Resource):
    @jwt_required
    def get(self, productid):
        cur.execute("SELECT * FROM products WHERE productid=%s", (productid,))
        products = cur.fetchone()
        if products is None:
            return jsonify({'message': 'Product not found!'})
        return jsonify(products)

    @jwt_required
    def put(self, productid):
        cur.execute("SELECT * FROM products WHERE productid=%s", (productid,))
        products = cur.fetchone()
        productname = request.get_json()['productname']
        quantity = request.get_json()['quantity']
        price = request.get_json()['price']


        if products is not None:
            cur.execute("UPDATE products SET productname=%s, quantity=%s, price=%s WHERE productid=%s", (productname, quantity, price, productid,))
            return jsonify({'message': 'Product updated successfully created '})
        conn.commit()

    @jwt_required
    def delete(self, productid):
        cur.execute("DELETE FROM products WHERE productid=%s", (productid,))
        conn.commit()