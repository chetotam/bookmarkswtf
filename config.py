''''''
from enum import Enum

class BaseConfig:
    ''''''
    SECRET_KEY = 'DRAKONKAPUSTA'

class DevelopmentConfig(BaseConfig):
    ''''''
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0 # Do not cache static files on client
    MONGODB_DB = 'bookmarkswtf-dev'

class TestingConfig(BaseConfig):
    ''''''
    TESTING = True

class ProductionConfig(BaseConfig):
    ''''''
    pass

class Config(Enum):
    ''''''
    DEVELOPMENT = DevelopmentConfig()
    TESTING = TestingConfig()
    PRODUCTION = ProductionConfig()

    DEFAULT = DevelopmentConfig()
