from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
db = PyMongo()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])

    # initialise app
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
