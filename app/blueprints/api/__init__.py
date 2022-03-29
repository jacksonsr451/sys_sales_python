from flask import Blueprint
from flask_restful import Api

from app.blueprints.api.user_resource import RegisterUserResource, DeleteUserResource, ListUsersResource, \
    GetUserByIDResource

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(RegisterUserResource, "/user")
api.add_resource(DeleteUserResource, "/user/delete/<id>")
api.add_resource(ListUsersResource, "/user/list")
api.add_resource(GetUserByIDResource, "/user/<id>")


def init_app(app):
    app.register_blueprint(blueprint=blueprint)
