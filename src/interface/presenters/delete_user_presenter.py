from src.applications.usecases.delete_user_by_id.delete_user_by_id_presenter_interface import DeleteUserByIDPresenterInterface


class DeleteUserByIDByIDPresenter(DeleteUserByIDPresenterInterface):
    def __init__(self):
        self.value: bool = False
        self.code = 409

    def present(self, value: bool):
        self.value = value

    def get_view_model(self):
        if self.value:
            self.code = 200
        return {"result": self.value}, self.code
