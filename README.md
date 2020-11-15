# Flask RESTplus API Skeleton code


## Application Stack

The Application Tech Stack includes:
- **Python3**: The [server language](https://www.python.org/downloads/)
- **Flask**: [Server Framework](https://flask.palletsprojects.com/en/1.1.x/)
- **PostgreSQL**: [Database](https://www.postgresql.org/) of choice
- **SQLAlchemy**: [ORM of choice](https://www.sqlalchemy.org/) to communicate between the python server and the Postgres Database. [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is directly used.
- **Heroku**: [Deployment Platform](https://www.heroku.com/)
- **[Postman](https://www.postman.com/)**: Testing the Application Endpoints

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