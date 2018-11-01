import os
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, verify_jwt_in_request, get_jwt_claims )



from db_conn import *
from app.api.v2.models.models import Products, UserModel, Sales
from functools import wraps



def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['role'] != 'Admin':
            return jsonify(msg='Admins only!'), 403
        else:
            return fn(*args, **kwargs)

    return wrapper


#@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity == 'admin':
        return {'role': 'Admin'}
    else:
        return {'role': 'Attendant'}


class Signup(Resource):

    @admin_required
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        role = data['role']
        user = UserModel(username, email, password, role)
        user.saveuser()
        return jsonify({'message': 'New user created!!!'})

    @jwt_required
    def get(self):
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        if users is None:
            return jsonify ({'message' : 'No users found'})
        all_products = []
        for user in users:
            format_p = {
                "username":user[0],
                "email":user[1],
                "password":user[2],
                "role":user[3],
                "date":user[4]
            }
            all_products.append(format_p)
        return all_products

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
        data = request.get_json()
        productname = data['productname']
        quantity = data['quantity']
        price = data['price']
        products = Products(productname,quantity,price)
        products.savedata()
        return jsonify({'message': 'Product successfully created '})

    @jwt_required
    def get(self):
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()

        if products is None:
            return jsonify ({'message' : 'No products found'})
        all_products = []
        for p in products:
            format_p = {
                "product_id":p[0],
                "name":p[1],
                "quantity":p[2],
                "price":p[3],
                "date":p[4]
            }
            all_products.append(format_p)
        return all_products








class Product(Resource):
    @jwt_required
    def get(self, productid):
        cur.execute("SELECT * FROM products WHERE productid=%s", (productid,))
        product = cur.fetchone()
        if product is None:
            return jsonify({'message': 'Product not found!'})

        format_p = {
                "product_id": product[0],
                "name": product[1],
                "quantity": product[2],
                "price": product[3],
                "date": product[4]
        }
        return jsonify({'success': True, 'products': format_p})

    # @jwt_required
    def put(self, productid):

        productname = request.get_json()['productname']
        quantity = request.get_json()['quantity']
        price = request.get_json()['price']

        cur.execute("SELECT * FROM products WHERE productid=%s", (productid,))
        product = cur.fetchone()
        print(product)

        if product is not None:
            x = cur.execute("UPDATE  products SET productname=%s, quantity=%s, price=%s WHERE productid=%s", (productname, quantity, price, productid,))
            conn.commit()

            return jsonify({'message': 'Product updated successfully created '})
        format_p = {
                "product_id": product[0],
                "name": product[1],
                "quantity": product[2],
                "price": product[3],
                "date": product[4]
        }
        return jsonify({'success': True, 'products': format_p})


    # @jwt_required
    def delete(self, productid):
        cur.execute("SELECT * FROM products WHERE productid=%s", (productid,))
        product = cur.fetchone()

        if product is not None:
            cur.execute("DELETE FROM products WHERE productid=%s", (productid,))
        else:
            return jsonify({'message': 'Productid not found'})

        format_p = {
                "product_id": product[0],
                "name": product[1],
                "quantity": product[2],
                "price": product[3],
                "date": product[4]
        }
        conn.commit()
        return jsonify ({'message': 'Product deleted successfully '})


class SalesList (Resource):

    @jwt_required
    def post(self):
        data = request.get_json()
        productname = data['product']
        quantity = data['quantity']
        price = data['price']
        sold_by = data['sold_by']
        sales = Sales(productname,quantity,price,sold_by)
        sales.savedata()
        return jsonify({'message': 'Product successfully created '})

    @jwt_required
    def get(self):
        cur.execute("SELECT * FROM sales")
        sales = cur.fetchall()

        if sales is not None:
            all_sales = []
            for sale in sales:
                format_p = {
                "sales_id": sale[0],
                "product": sale[1],
                "quantity": sale[2],
                "price": sale[3],
                "sold_by": sale[4],
                "date": sale[5]
                }
                all_sales.append(format_p)
            return all_sales
        else:
            return jsonify({'message': 'No sales found'})

class Sale(Resource):
    @jwt_required
    def get(self, salesid):
        cur.execute("SELECT * FROM sales WHERE salesid=%s", (salesid,))
        sale = cur.fetchone()
        if sale is not None:
            format_p = {
            "sales_id": sale[0],
            "product": sale[1],
            "quantity": sale[2],
            "price": sale[3],
            "sold_by": sale[4],
            "date": sale[5]
            }
            return jsonify({'success': True, 'products': format_p})
        else:
            return jsonify({'message': 'Sale not found!'})


