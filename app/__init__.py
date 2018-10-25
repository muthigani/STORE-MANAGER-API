from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import app_config



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])

    #from app.api.v1 import version1 as v1

    from app.api.v2 import version2 as v2

    # register the blueprints
    #app.register_blueprint(v1)

    app.register_blueprint(v2)

    app.config['JWT_SECRET_KEY'] = 'makorokocho'
    jwt = JWTManager(app)


    return app