''''''
from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from .main import main

db = MongoEngine()

def create_app(config=Config.DEFAULT):
    ''''''
    app = Flask(__name__)
    app.config.from_object(config.value)
    app.register_blueprint(main)
    db.init_app(app)
    return app
