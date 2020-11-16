"""
The Data transfer object (DTO) will be responsible for carrying data between \
processes. In this case, it will be used for marshaling data for our API calls
"""

from flask_restplus import Namespace, fields


class UserDto:
    """
    Creates a new namespace for user related operations. Flask-RESTPlus \
    provides a way to use almost the same pattern as Blueprint. The main \
    idea is to split your app into reusable namespaces. A namespace module \
    will contain models and resources declaration.\n
    The next line reates a new user dto through the model interface provided \
    by the api namespace.
    """
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })