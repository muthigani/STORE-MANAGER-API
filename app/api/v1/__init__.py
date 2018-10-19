from flask import Blueprint
from flask_restful import Api

from app.api.v1.views import Sales, SalesList, Product, ProductList

version1 = Blueprint('api',__name__, url_prefix ='/api/v1')
api = Api(version1)

api.add_resource(Sales, '/sales/<int:salesid>')
api.add_resource(SalesList, '/sales')

api.add_resource(Product, '/products/<int:productid>')
api.add_resource(ProductList, '/products')



