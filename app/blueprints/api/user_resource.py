from flask import jsonify, request
from flask_restful import Resource

from src.infrastructure.repositories.users_repository import UsersRepository
from src.interface.controllers.registration_controller import RegistrationController
from src.interface.presenters.registration_presenter import RegistrationPresenter


class UserResource(Resource):
    @classmethod
    def post(cls):
        print(request.get_json())
        controller = RegistrationController(request=request.get_json(), repository=UsersRepository())
        presenter = RegistrationPresenter()
        controller.register(presenter=presenter)
        return jsonify(presenter.get_view_model())
