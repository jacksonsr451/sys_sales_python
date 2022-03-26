from flask_sqlalchemy import SQLAlchemy

data_base = SQLAlchemy()


def init_app(app):
    data_base.init_app(app=app)

