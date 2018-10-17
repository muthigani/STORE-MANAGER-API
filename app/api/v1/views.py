from flask import Flask
from flask_restful import Api, Resource, reqparse

orders = []


class OrderList(Resource):
    def get(self):
        return orders, 200


class Order(Resource):
    def get(self, orderid):
        for order in orders:
            if (orderid == order["orderid"]):
                return order, 200
            return "User not found", 404

    def post(self, orderid):
        parser = reqparse.RequestParser()
        parser.add_argument("food")
        parser.add_argument("clientname")
        parser.add_argument("location")
        parser.add_argument("phone")
        parser.add_argument("quantity")
        parser.add_argument("price")
        parser.add_argument("orderstat")
        args = parser.parse_args()

        for order in orders:
            if (orderid == order["orderid"]):
                return "order with ID number {} already exists".format(orderid), 400

        order = {
            "orderid": orderid,
            "food": args["food"],
            "clientname": args["clientname"],
            "location": args["location"],
            "phone": args["phone"],
            "quantity": args["quantity"],
            "price": args["price"],
            "orderstat": args["orderstat"],

        }
        orders.append(order)
        return order, 201

    def put(self, orderid):
        parser = reqparse.RequestParser()
        parser.add_argument("food")
        parser.add_argument("clientname")
        parser.add_argument("location")
        parser.add_argument("phone")
        parser.add_argument("quantity")
        parser.add_argument("price")
        parser.add_argument("orderstat")
        args = parser.parse_args()

        for order in orders:
            if (orderid == order["orderid"]):
                order["food"] = args["food"]
                order["clientname"] = args["clientname"]
                order["location"] = args["location"]
                order["phone"] = args["phone"]
                order["quantity"] = args["quantity"]
                order["price"] = args["price"]
                order["orderstat"] = args["orderstat"]
                return order, 200

        order = {
            "orderid": orderid,
            "food": args["food"],
            "clientname": args["clientname"],
            "location": args["location"],
            "phone": args["phone"],
            "quantity": args["quantity"],
            "price": args["price"],
            "orderstat": args["orderstat"],

        }

        orders.append(order)
        return order, 201
