''''''
from flask_login import AnonymousUserMixin, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager


class Bookmark(db.EmbeddedDocument):
    ''''''
    url = db.URLField(required=True)
    title = db.StringField(required=True)
    description = db.StringField(default='', required=True)
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

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return str(self.id)

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        ''''''
        try:
            return User.objects.get(id=user_id)
        except db.DoesNotExist:
            return None
