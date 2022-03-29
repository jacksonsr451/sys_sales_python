from app.blueprints.api.user_resource import ListUsersResource, DeleteUserResource, RegisterUserResource, \
    GetUserByIDResource

api_routes = [
    (RegisterUserResource, "/user"),
    (DeleteUserResource, "/user/delete/<id>"),
    (ListUsersResource, "/user/list"),
    (GetUserByIDResource, "/user/<id>")
]

web_routes = []
