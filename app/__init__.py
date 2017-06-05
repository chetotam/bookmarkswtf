''''''
from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

from config import Config


db = MongoEngine()
login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'

def create_app(config=Config.DEFAULT):
    ''''''
    app = Flask(__name__)
    app.config.from_object(config.value)

    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth)

    db.init_app(app)
    login_manager.init_app(app)

    return app
