import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    """
    Creates a new user by first checking if the user already exists. It \
    returns a success response_object if the user doesn’t exist else it \
    returns an error code 409 and a failure response_object.
    """
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        # No need to use jsonify for formatting an object to JSON,
        # Flask-restplus does it automatically
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """
    Returns all the users in the database
    """
    return User.query.all()


def get_a_user(public_id):
    """
    Get a user by their public_id
    """
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    """
    Commit a new user to the database
    """
    db.session.add(data)
    db.session.commit()