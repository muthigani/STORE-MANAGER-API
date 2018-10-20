from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1.views.views import ProductsList, Product, SalesList, Sale
from app.api.v1.views.users import Register, Login 

# obtain the blueprint by initialising
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)



# specific endpoints
api.add_resource(SalesList, '/sales')
api.add_resource(Sale, '/sales/<salesid>')
api.add_resource(ProductsList, '/products')
api.add_resource(Product, '/products/<productid>')
api.add_resource(Register, '/authorization/register')
api.add_resource(Login, '/authorization/login')
