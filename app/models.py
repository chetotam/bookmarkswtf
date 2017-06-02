''''''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

class Bookmark(db.EmbeddedDocument):
    ''''''
    title = db.StringField(required=True)
    description = db.StringField(default='', required=True)
    url = db.URLField(required=True)
    date_last_viewed = db.DateTimeField(required=True)

class UserPermissionLevel(db.EmbeddedDocument):
    ''''''
    pass

class User(db.Document, UserMixin):
    ''''''
    meta = {'collection': 'users'}

    email = db.EmailField(unique=True, required=True)
    password_hash = db.StringField(required=True)
    bookmarks = db.ListField(db.EmbeddedDocumentField(Bookmark))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
