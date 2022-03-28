from app.data.models.users import Users
from app.extensions.flask_marshmallow import marshmallow


class UserSchema(marshmallow.Schema):
    class Meta:
        model = Users
        load_instance = True
        fields = ['id', 'username', 'email']
