'''Contains MongoEngine data models.'''
from datetime import datetime

from flask_login import AnonymousUserMixin, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager


class Bookmark(db.EmbeddedDocument):
    '''Represents bookmark.'''

    url = db.URLField(required=True)
    # TODO: somehow retrieve title from page mb
    title = db.StringField(required=True)
    description = db.StringField(default='', required=True)
    date_last_viewed = db.DateTimeField(default=datetime.now(), required=True)
    # TODO: add property to display time left before bookmark gets deleted mb

    def __init__(self, *, url, title, **kwargs):
        # TODO: check this works ok
        super().__init__(**kwargs)
        self.url = url
        self.title = title

    @property
    def time_left(self):
        '''Returns time left before bookmark gets deleted.'''
        # TODO: check this works ok for different timezones
        return datetime.now() - self.date_last_viewed

    @property
    def expired(self):
        '''Returns True if bookmark lifetime exceeded tresshold'''
        # TODO: make bookmark lifetime configurable
        return self.time_left.days > 30

    def __repr__(self):
        return '<Bookmark {}>'.format(self.url)


class UserPermissionLevel(db.EmbeddedDocument):
    '''Represents user permissions.'''
    # TODO: think if this kind of service needs different permission levels
    pass


class User(db.Document, UserMixin):
    '''Represents user.'''

    # TODO: check how to use init method on MongoEngine.Document objects like this
    # with custom properties and stuff
    meta = {'collection': 'users'}

    email = db.EmailField(unique=True, required=True)
    password_hash = db.StringField(required=True)
    bookmarks = db.SortedListField(
        db.EmbeddedDocumentField(Bookmark), ordering='date_last_viewed', reverse=True)
    # TODO: think if user needs some kind of personal information like name or profile picture

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # TODO: check which UserMixin methods i actually need to redefine
    @property
    def is_active(self):
        # do i need email confirmation for this?
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
        '''User loader function for Flask-Login'''
        try:
            return User.objects.get(id=user_id)
        except db.DoesNotExist:
            return None

    def __repr__(self):
        return '<User {}>'.format(self.email)
