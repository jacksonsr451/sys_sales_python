from flask import Blueprint

blueprint = Blueprint("web", __name__)


def init_app(app):
    app.register_blueprint(blueprint=blueprint)
