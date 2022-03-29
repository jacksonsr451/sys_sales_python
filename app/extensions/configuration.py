from importlib import import_module

from dynaconf import FlaskDynaconf


def load_extensions(app):
    print(app.config)
    for extension in app.config.EXTENSIONS:
        ext = import_module(extension)
        ext.init_app(app)


def init_web_routes(app, routes):
    pass


def init_api_routes(api, routes):
    for get_route in routes:
        controller, route = get_route
        api.add_resource(controller, route)


def init_app(app):
    FlaskDynaconf(app)
