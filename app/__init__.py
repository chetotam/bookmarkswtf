''''''
from flask import Flask
from config import Config
from .main import main

def create_app(config=Config.DEFAULT):
    ''''''
    app = Flask(__name__)
    app.config.from_object(config.value)
    app.register_blueprint(main)
    return app
