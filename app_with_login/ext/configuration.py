from dynaconf import FlaskDynaconf


def init_app(app, **config):
    FlaskDynaconf(app, **config)

    DB_USER = app.config['DB_USER']
    DB_PASSWORD = app.config['DB_PASSWORD']
    DB_URL = app.config['DB_URL']
    DB_NAME = app.config['DB_NAME']
    DB_CONNECTOR = app.config['DB_CONNECTOR']

    app.config['SQLALCHEMY_DATABASE_URI'] = f"{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}"
    app.config.load_extensions()
