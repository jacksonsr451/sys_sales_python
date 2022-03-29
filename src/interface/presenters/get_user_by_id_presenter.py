from src.applications.usecases.get_user_by_id.get_user_by_id_presenter_interface import GetUserByIDPresenterInterface


class GetUserByIDPresenter(GetUserByIDPresenterInterface):
    def __init__(self):
        self.user = None
        self.code = 400

    def present(self, user):
        self.user = user

    def get_view_model(self):
        if self.user is not None:
            self.code = 200
        return self.user, self.code
