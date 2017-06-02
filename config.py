''''''
from enum import Enum

class BaseConfig:
    ''''''
    SECRET_KEY = 'DRAKONKAPUSTA'

class DevelopmentConfig(BaseConfig):
    ''''''
    DEBUG = True
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
