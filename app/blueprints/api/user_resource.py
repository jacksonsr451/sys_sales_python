from flask import jsonify, request
from flask_restful import Resource

from __tests__.application.usecases.test_delete_user_by_id import DeleteUserByIDPresenter
from src.infrastructure.repositories.users_repository import UserRepository
from src.interface.controllers.delete_user_by_id_controller import DeleteUserByIDController
from src.interface.controllers.register_user_controller import RegistrationController
from src.interface.presenters.register_user_presenter import RegisterUserPresenter


class RegisterUserResource(Resource):
    @classmethod
    def post(cls):
        controller = RegistrationController(request=request.get_json(), repository=UserRepository())
        presenter = RegisterUserPresenter()
        controller.register(presenter=presenter)
        return jsonify(presenter.get_view_model())


class DeleteUserResource(Resource):
    @classmethod
    def delete(cls, id):
        controller = DeleteUserByIDController(id=id, repository=UserRepository())
        presenter = DeleteUserByIDPresenter()
        controller.delete(presenter=presenter)
        return jsonify(presenter.get_view_model())
