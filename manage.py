''''''
from flask_script import Manager, Server
from app import create_app, db
from app.models import User, Bookmark

manager = Manager(create_app)
manager.add_command('runserver', Server())

@manager.shell
def make_shell_context():
    ''''''
    return dict(app=manager.app, db=db, User=User, Bookmark=Bookmark)

@manager.command
def test():
    '''Run the unit tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
