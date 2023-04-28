import os
from dotenv import load_dotenv


load_dotenv()

ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
CONFIG_NAME = os.environ["CONFIG_NAME"]

FLASK_ADMIN_SWATCH = 'cosmo'


OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_VERSION = '3.0.0'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = os.environ["SECRET_KEY"]
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]


class TestingConfig(BaseConfig):
    TESTING = True