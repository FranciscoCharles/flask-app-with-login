from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from app_with_login.ext.database import db
from app_with_login.models import User
import toml

def create_db_if_not_exists():
    all_settings = toml.load('settings.toml')
    default_settings = all_settings['default']

    DB_USER = default_settings['DB_USER']
    DB_PASSWORD = default_settings['DB_PASSWORD']
    DB_URL = default_settings['DB_URL']
    DB_NAME = default_settings['DB_NAME']
    DB_CONNECTOR = default_settings['DB_CONNECTOR']

    full_db_url = f"{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_URL}"
    engine = create_engine(full_db_url, echo=True)
    engine.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
    engine.dispose()
    
def create_db():
    """Creates database"""
    try:
        create_db_if_not_exists()
        db.create_all()
    except SQLAlchemyError as error:
        print('Create DB error:', error)
    #User.__table__.create(engine)

def drop_db():
    """Drop database"""
    try:
        db.drop_all()
    except SQLAlchemyError as error:
        print('Drop DB error:', error)
    #User.__table__.drop(engine)

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