from app.data.models.users import Users


class UserModelAdapter(Users):
    @classmethod
    def find_by_id(cls, id: str):
        return Users.query.filter_by(id=id).first()

    @classmethod
    def find_by_username(cls, username: str):
        return Users.query.filter_by(username=username).first()
