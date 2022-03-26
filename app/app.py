from flask import Flask

from app.extensions import configuration


def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app=app)
    return app


def create_app():
    app = minimal_app()
    configuration.load_extensions(app=app)
    app.app_context().push()
    return app
