from src.applications.usecases.delete_user_by_id.delete_user_by_id_presenter_interface import DeleteUserByIDPresenterInterface


class DeleteUserByIDByIDPresenter(DeleteUserByIDPresenterInterface):
    def __init__(self):
        self.value: bool = False

    def present(self, value: bool):
        self.value = value

    def get_view_model(self):
        return self.value
