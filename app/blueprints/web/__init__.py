from flask import Blueprint

web = Blueprint("web", __name__)


def get_web_app():
    return web


def init_app(app):
    app.register_blueprint(web)
