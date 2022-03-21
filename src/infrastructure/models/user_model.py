from src.infrastructure.models.model_factoring import ModelFactoring


class UserModel(ModelFactoring):
    def __init__(self):
        super(UserModel, self).__init__()
        self.table_name = "users"
        self.table(
            [
                "id text PRIMARY KEY",
                "username text NOT NULL UNIQUE",
                "email text NOT NULL UNIQUE",
                "password text NOT NULL"
            ]
        )
