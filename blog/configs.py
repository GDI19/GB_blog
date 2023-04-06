import os
from dotenv import load_dotenv


load_dotenv()

ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
CONFIG_NAME = os.environ["CONFIG_NAME"]


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