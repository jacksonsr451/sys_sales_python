from flask import jsonify, request
from flask_restful import Resource

from src.infrastructure.repositories.users_repository import UserRepository
from src.interface.controllers.register_user_controller import RegistrationController
from src.interface.presenters.register_user_presenter import RegisterUserPresenter


class UserResource(Resource):
    @classmethod
    def post(cls):
        print(request.get_json())
        controller = RegistrationController(request=request.get_json(), repository=UserRepository())
        presenter = RegisterUserPresenter()
        controller.register(presenter=presenter)
        return jsonify(presenter.get_view_model())
