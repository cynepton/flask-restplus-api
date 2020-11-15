# Flask RESTplus API Skeleton code

The Application uses the [Flask RESTplus extension](https://flask-restplus.readthedocs.io/) and a [functional structure](http://exploreflask.com/en/latest/blueprints.html#functional-structure) to organize the project. In a functional structure, templates are grouped together in one directory, static files in another and views in a third.

## Application Stack

The Application Tech Stack includes:
- **Python3**: The [server language](https://www.python.org/downloads/)
- **Flask**: [Server Framework](https://flask.palletsprojects.com/en/1.1.x/)
- **PostgreSQL**: [Database](https://www.postgresql.org/) of choice
- **SQLAlchemy**: [ORM of choice](https://www.sqlalchemy.org/) to communicate between the python server and the Postgres Database. [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is directly used.
- **Heroku**: [Deployment Platform](https://www.heroku.com/)
- **[Postman](https://www.postman.com/)**: Testing the Application Endpoints

### Extensions
- **Flask-Bcrypt**: A [Flask extension that provides bcrypt hashing utilities](https://flask-bcrypt.readthedocs.io/) for your application.
- **Flask-Migrate**: An [extension that handles SQLAlchemy database migrations for Flask applications using Alembic](https://flask-migrate.readthedocs.io/). The database operations are made available through the Flask command-line interface or through the Flask-Script extension.
- **Flask-SQLAlchemy**: An [extension for Flask that adds support for SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) to your application.
- **PyJWT**: A [Python library which allows you to encode and decode JSON Web Tokens (JWT)](https://pyjwt.readthedocs.io/). JWT is an open, industry-standard (RFC 7519) for representing claims securely between two parties.
- **Flask-Script**: [An extension that provides support for writing external scripts in Flask](https://flask-script.readthedocs.io/) and other command-line tasks that belong outside the web application itself.
- **Flask-RESTPlus**: An [extension for Flask that adds support for quickly building REST APIs](https://flask-restplus.readthedocs.io/). Flask-RESTPlus encourages best practices with minimal setup. It provides a coherent collection of decorators and tools to describe your API and expose its documentation properly (using Swagger).

## Working with the application locally
Make sure you have [Python](https://www.python.org/downloads/) installed.

1. **Clone the Repository**
    ```bash
    git clone -b main https://github.com/cynepton/flask-restplus-api.git
    ```

2. **Set up a virtual environment**:
    ```bash
    virtualenv env
    source env/Scripts/activate # for windows
    source env/bin/activate # for MacOs
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Export Environment Variables**
    Refer to the `setup.bash` file and export the environment variables for the project.

5. **Create Local Database**:
    Create a local database and export the database URI as an environment variable with the key `DATABASE_PATH`.

6. **Run Database Migrations**:
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

7. **Run the Flask Application locally**:
    ```bash
    export FLASK_APP=myapp
    export FLASK_ENV=development
    flask run
    ```

## Endpoints