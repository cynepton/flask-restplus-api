from .. import db, flask_bcrypt

class User(db.Model):
    """
    User Model for storing user related details
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        """
        This would return an error, password is write only
        """
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        """
        Password setter that uses flask bcrypt to generate a has using the\
        provided password
        """
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """
        Returns a boolean, that is true if the user's password is correct.
        """
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)