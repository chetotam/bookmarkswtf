''''''
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config
from .main import main
from .auth import auth

db = MongoEngine()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config=Config.DEFAULT):
    ''''''
    app = Flask(__name__)
    app.config.from_object(config.value)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    db.init_app(app)
    login_manager.init_app(app)
    return app
