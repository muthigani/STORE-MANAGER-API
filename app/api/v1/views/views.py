from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)


# ProductsList lists
#products=ProductsData().get_products()
#SALES
sales = []


class SalesList(Resource):

    @jwt_required
    def get(self):
        """
            Obtain  sales
        """
        return jsonify({
            'status': 'OK',
            'SalesList': sales
        })
    @jwt_required
    def post(self):
        """create a sales"""
        data = request.get_json()

        # users data entered, stored in variables
        salesid = len(sales)+1
        category = data['category']
        sale_name = data['product_name']
        quantity = data['quantity']
        price = data['price']

        # check if product is available in the products list

        # store products in a dictionary
        sale = {
            "salesid": salesid,
            "category": category,
            "product_name": sale_name,
            "quantity": quantity,
            "price": price
        }
        # add sales product to the sales list
        sales.append(sale)

        # message to be displayed
        return jsonify({'response': 'New Sale recorded'})


class Sale(Resource):
    @jwt_required
    def get(self, salesid):
        """
            Get only a single sales using saleid
            param : Store Owner/admin and store attendant of the specific sales record
        """
        for sale in sales:
            if int(sale["salesid"]) == int(salesid):
                return make_response(jsonify(
            {
                'status': 'OK',
                'My sale':sale
            }
            ),200)
        else:
            return jsonify({"response": "Sale Not Available"})



# PRODUCT
products =[]

class ProductsList(Resource):
    @jwt_required
    def get(self):
        """Fetch all products

        """
        return make_response(jsonify(
            {
                'status': 'OK',
                'ProductsList':products
            }
        ),200)

    @jwt_required
    def post(self):
        """post product to list
        """
        # fetch users input data
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"}) 
        productid = len(products)+1
        productname = data['productname']
        quantity = data['quantity']
        price = data['price']

        # dictionary data structure for users products
        product = {
            "productid":productid,
            "productname": productname,
            "quantity":quantity,
            "price":price,
        }
        # Store products obtained from the user in a list
        products.append(product)

        # message to be displayed to the user
        return jsonify( {'response':'New product added successfully'})
    
class Product(Resource):
    ''' get a single product '''
    @jwt_required
    def get(self, productid):
        """Get a single product record"""
        for product in products:
            if int(product["productid"]) == int(productid):
                return make_response(jsonify(
            {
                'status': 'OK',
                'My product':product
            }
            ),200)
        else:
            return jsonify({"response": "Product Not Available"})