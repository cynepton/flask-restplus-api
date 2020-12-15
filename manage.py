import os
import unittest

"""
Flask-Migrate exposes two classes, Migrate and MigrateCommand.\n
The Migrateclass contains all the functionality of the extension.\n
The MigrateCommand class is only used when it is desired to expose database \
migration commands through the Flask-Script extension.
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model import user
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

# Instantiate the manager class and bind it to the flask app
manager = Manager(app)

# Instantiate the migrate class and bind it to the flask app ans sqlalchemy db
migrate = Migrate(app, db)

# Expose database migrate commands through flask script
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    """
    Defines the run function to run the flask app using:\n
        python manage.py run\n
    From the terminal.
    """
    app.run()

@manager.command
def test():
    """
    Runs the unit tests.
    """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()