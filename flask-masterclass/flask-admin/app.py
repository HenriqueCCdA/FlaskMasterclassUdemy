import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
    app.config['SECRET_KEY'] = 'chave secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['DATABASE_TRACT_MODIFICATONS']

    admin = Admin(app, name='Spacedevs', template_mode="bootstrap3")
    db.init_app(app)

    from models import User

    admin.add_view(ModelView(User, db.session))

    return app
