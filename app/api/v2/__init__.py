from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.views import ProductsList, Product, Signup, Login

# obtain the blueprint by initialising
version2 = Blueprint('api', __name__, url_prefix='/api/v2')
api = Api(version2)



# specific endpoints
#api.add_resource(SalesList, '/sales')
#api.add_resource(Sale, '/sales/<salesid>')
api.add_resource(ProductsList, '/products')
api.add_resource(Product, '/products/<productid>')
api.add_resource(Signup, '/auth/signup')
api.add_resource(Login, '/auth/login')