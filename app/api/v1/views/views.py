from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)



#SALES
sales = []


class SalesList(Resource):
    @jwt_required
    def get(self):
        """
            Obtain  sales
        """
        return jsonify({
            'SalesList': sales
        })
    @jwt_required
    def post(self):
        """create a sales"""
        data = request.get_json()

        # users data entered, stored in variables
        sales_id = len(sales)
        category = data['category']
        productname = data['productname']
        quantity = data['quantity']
        price = data['price']

        # check if product is available in the products list

        # store products in a dictionary
        sale = {
            "salesId": sales_id,
            "category": category,
            "productname": productname,
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
            if sale['salesid'] == salesid:
                return jsonify({"response": sale})

        return jsonify({"response": "Product Not Available"})



# PRODUCT
products =[]

class ProductsList(Resource):
    @jwt_required
    def get(self):
        """Fetch all products

        """
        return make_response(jsonify(
            {
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
        productid = len(products)
        productname = data['productname']
        quantity = data['quantity']
        price = data['price']

        # data structure for users product
        product = {
            "productid": productid,
            "productname": productname,
            "quantity": quantity,
            "price":price,
        }
        # Store products obtained from the user in a list
        products.append(product)

        # message to be displayed to the user
        return jsonify( {'response':'New product added successfully'})
    
class Product(Resource):
    ''' fetch a single product '''
    @jwt_required
    def get(self, productid):
        """Get a single product record"""
        for product in products:
            if product['productid'] == productid:
                return jsonify(
                    {
                        'response':product
                    }
                )
        return jsonify({'response':'Product Not Available'})

