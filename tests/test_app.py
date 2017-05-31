''''''
from unittest import TestCase
from flask import current_app
from app import create_app
from config import Config

class AppTestCase(TestCase):
    ''''''
    def setUp(self):
        self.app = create_app(config=Config.TESTING)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        ''''''
        self.app_context.pop()

    def test_app_exists(self):
        ''''''
        self.assertFalse(current_app is None)
