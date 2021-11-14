from flask import current_app
from flask.cli import with_appcontext
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database, drop_database
from app_with_login.ext.database import db
from app_with_login.models import User


@with_appcontext
def create_db():
    """Creates database"""
    try:
        database_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
        if not database_exists(database_uri):
            create_database(database_uri)
        db.create_all()
    except SQLAlchemyError as error:
        print('Create DB error:', error)

@with_appcontext
def drop_db():
    """Drop database"""
    try:
        database_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
        if database_exists(database_uri):
            drop_database(database_uri)
    except SQLAlchemyError as error:
        print('Drop DB error:', error)

def populate_db():
    """Populate database"""
    data = [
        User(name="joel", email="joel@example.com", password="123"),
        User(name="ellie", email="ellie@example.com", password="123"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()

def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))