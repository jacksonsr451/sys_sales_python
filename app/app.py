from flask import Flask

from app.blueprints.api import api
from app.blueprints.web import web
from app.extensions import configuration
from app.routes import api_routes, web_routes


def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app=app)
    configuration.init_api_routes(api=api, routes=api_routes)
    configuration.init_web_routes(api=web, routes=web_routes)
    return app


def create_app():
    app = minimal_app()
    configuration.load_extensions(app=app)
    app.app_context().push()
    return app
