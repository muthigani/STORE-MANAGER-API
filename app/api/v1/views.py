from flask_restful import Resource, reqparse

# Sales Endpoints

sales = [
                {
					 "salesid": 1,
					 "productname" : "Samsung 8",
					 "clientname":"Martin Muriuki",
					 "phonenumber":"0722333456",
					 "quantity": 1,
					 "price":Ksh.80000,
				},
                {
					 "salesid": 2,
					 "productname" : "Samsung 9",
					 "clientname":"Peris Ndanu",
					 "phonenumber":"0711234554",
					 "quantity": 1,
					 "price":Ksh.90000,
				},
		]


class SalesList(Resource):
    def get(self):
        return sales, 200


class Sales(Resource):

    def get(self, salesid):
        for sale in sales:
            if salesid == sale["salesid"]:
                return sale, 200
            return "User not found", 404

    def post(self, salesid):
        parser = reqparse.RequestParser()
        parser.add_argument("productname")
        parser.add_argument("clientname")
        parser.add_argument("phonenumber")
        parser.add_argument("quantity")
        parser.add_argument("price")
        args = parser.parse_args()

        for sale in sales:
            if salesid == sale["salesid"]:
                return "order with ID number {} already exists".format(salesid), 400

        sale = {
            "salesid": salesid,
            "productname": args["productname"],
            "clientname": args["clientname"],
            "phonenumber": args["phonenumber"],
            "quantity": args["quantity"],
            "price": args["price"],


        }
        sales.append(sale)
        return sale, 201

    def put(self, salesid):
        parser = reqparse.RequestParser()
        parser.add_argument("productname")
        parser.add_argument("clientname")
        parser.add_argument("phonenumber")
        parser.add_argument("quantity")
        parser.add_argument("price")
        args = parser.parse_args()

        for sale in sales:
            if (salesid == sale["salesid"]):
                sale["productname"] = args["productname"]
                sale["clientname"] = args["clientname"]
                sale["phonenumber"] = args["phonenumber"]
                sale["quantity"] = args["quantity"]
                sale["price"] = args["price"]


        sale = {
                "salesid": salesid,
                "productname": args["productname"],
                "clientname": args["clientname"],
                "phonenumber": args["phonenumber"],
                "quantity": args["quantity"],
                "price": args["price"],
              }

        sales.append(sale)
        return sale, 201

# Product Endpoint

products = [
				{
					 "productid": 1,
					 "productname" : "Samsung S9",
					 "phonenumber":"0722123456",
					 "quantity": 15,
					 "price": 90000,
					 "status":"Product Available",
				},
				{
					 "productid": 2,
					 "productname" : "Samsung S8",
					 "phone":"0722123456",
					 "quantity": 1,
					 "price": 80000,
					 "status":"pending",
				},
			]


class ProductList(Resource):
    def get(self):
        return products, 200


class Product(Resource):
    def get(self, productid):
        for product in products:
            if productid == product["productid"]:
                return product, 200
            return "User not found", 404

    def post(self, productid):
        parser = reqparse.RequestParser()
        parser.add_argument("productname")
        parser.add_argument("quantity")
        parser.add_argument("price")
        parser.add_argument("status")
        args = parser.parse_args()

        for product in products:
            if productid == product["productid"]:
                return "product with ID number {} already exists".format(productid), 400

        product = {
            "productid": productid,
            "productname": args["productname"],
            "quantity": args["quantity"],
            "price": args["price"],
            "status": args["status"],

        }
        products.append(product)
        return product, 201

    def put(self, productid):
        parser = reqparse.RequestParser()
        parser.add_argument("productname")
        parser.add_argument("quantity")
        parser.add_argument("price")
        parser.add_argument("status")
        args = parser.parse_args()

        for product in products:
            if productid == product["productid"]:
                product["productname"] = args["productname"]
                product["quantity"] = args["quantity"]
                product["price"] = args["price"]
                product["status"] = args["status"]
                return product, 200

        product = {
            "productid": productid,
            "productname": args["productname"],
            "quantity": args["quantity"],
            "price": args["price"],
            "status": args["status"],

        }

        products.append(product)
        return product, 201
