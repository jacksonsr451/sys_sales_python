from flask import Blueprint
from flask_restful import Api

from app.blueprints.api.user_resource import UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(UserResource, "/user")


def init_app(app):
    app.register_blueprint(blueprint=blueprint)
