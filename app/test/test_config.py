"""
This script runs tests for the config file in the main application.
"""
import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir


class TestDevelopmentConfig(TestCase):
    """
    This class tests the development environment configuration
    """
    def create_app(self):
        """
        This function gets the configuration details from the\
        DevelopmentConfig class in the main application's config file.
        """
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        """
        Test cases
        """
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()