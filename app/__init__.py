from flask import Flask, Blueprint
from config import api_config


def create_app(config_filename):
    app = Flask(__name__)

    #app.config.from_object('config')


    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)



    return app

