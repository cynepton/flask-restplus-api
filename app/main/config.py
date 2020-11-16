import os

# Database URLs
# This checks the environment variables for the Database URL
# Uncomment below for postgres database 
# DATABASE_URL = os.environ['DATABASE_URL']
# DEV_DB = os.environ['DEVELOPMENT_DATABASE']
# TEST_DB = os.environ['TEST_DATABASE']

basedir = os.path.abspath(os.path.dirname(__file__))
DEV_DB = 'sqlite:///' + os.path.join(basedir, 'flask_main.db')
TEST_DB = 'sqlite:///' + os.path.join(basedir, 'flask_test.db')

class Config:
    """
    Base config class for the Flask App configuration
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_so_very_secretive_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Application configuration for the development environment
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DEV_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Application configuration for the Testing Environment
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DB
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Application configuration for the Production environment
    """
    DEBUG = False
    # Uncomment for the Postgres production database
    # SQLALCHEMY_DATABASE_URI = DATABASE_URL


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY