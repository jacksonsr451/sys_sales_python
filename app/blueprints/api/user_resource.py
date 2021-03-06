from flask import jsonify, request, make_response
from flask_restful import Resource

from app.schemas.user_schema import UserSchema
from src.infrastructure.repositories.users_repository import UserRepository
from src.interface.controllers.delete_user_by_id_controller import DeleteUserByIDController
from src.interface.controllers.get_user_by_id_controller import GetUserByIDController
from src.interface.controllers.list_users_controller import ListUsersController
from src.interface.controllers.register_user_controller import RegistrationController
from src.interface.presenters.delete_user_presenter import DeleteUserByIDPresenter
from src.interface.presenters.get_user_by_id_presenter import GetUserByIDPresenter
from src.interface.presenters.list_users_presenter import ListUsersPresenter
from src.interface.presenters.register_user_presenter import RegisterUserPresenter


class RegisterUserResource(Resource):
    @classmethod
    def post(cls):
        controller = RegistrationController(request=request.get_json(), repository=UserRepository())
        presenter = RegisterUserPresenter()
        controller.register(presenter=presenter)
        data, statuscode = presenter.get_view_model()
        return make_response(jsonify(data), statuscode)


class DeleteUserResource(Resource):
    @classmethod
    def delete(cls, id):
        controller = DeleteUserByIDController(id=id, repository=UserRepository())
        presenter = DeleteUserByIDPresenter()
        controller.delete(presenter=presenter)
        data, statuscode = presenter.get_view_model()
        return make_response(jsonify(data), statuscode)


class ListUsersResource(Resource):
    @classmethod
    def get(cls):
        controller = ListUsersController(repository=UserRepository())
        presenter = ListUsersPresenter()
        controller.list(presenter=presenter)
        user_schema = UserSchema(many=True)
        data, statuscode = presenter.get_view_model()
        return make_response(jsonify(user_schema.dump(data)), statuscode)


class GetUserByIDResource(Resource):
    @classmethod
    def get(cls, id):
        controller = GetUserByIDController(repository=UserRepository())
        presenter = GetUserByIDPresenter()
        controller.get_user(id=id, presenter=presenter)
        user_schema = UserSchema()
        data, statuscode = presenter.get_view_model()
        return make_response(jsonify(user_schema.dump(data)), statuscode)
