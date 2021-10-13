import toml
from sqlalchemy import create_engine
from app_with_login.models import User
from app_with_login.ext.database import db


all_settings = toml.load('settings.toml')
default_settings = all_settings['default']

DB_USER = default_settings['DB_USER']
DB_PASSWORD = default_settings['DB_PASSWORD']
DB_URL = default_settings['DB_URL']
DB_NAME = default_settings['DB_NAME']
DB_CONNECTOR = default_settings['DB_CONNECTOR']

DB_URI = f"{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}"
engine = create_engine(DB_URI, echo=True)

def create_db():
    """Creates database"""
    db.create_all()
    #User.__table__.create(engine)

def drop_db():
    """Drop database"""
    db.drop_all()
    #User.__table__.drop(engine)

def populate_db():
    """Populate database"""
    data = [
        User(name="joel", email="joel@example.com", password="123"),
        User(name="ellie", email="ellie@example.com", password="123"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()

def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))