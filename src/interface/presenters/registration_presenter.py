from src.applications.usecases.register_user.register_user_presenter_interface import RegisterUserPresenterInterface


class RegisterUserPresenter(RegisterUserPresenterInterface):
    def __init__(self):
        self.view_model: bool = False
        self.code = 409

    def present(self, registration: bool):
        self.view_model = registration

    def get_view_model(self):
        if self.view_model:
            self.code = 200
        return {"result": self.view_model}, self.code
