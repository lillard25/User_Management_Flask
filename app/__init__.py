from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()
swagger = Swagger()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)

    # Swagger UI configuration
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Flask Application"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    from app.routes import main
    app.register_blueprint(main)

    return app
