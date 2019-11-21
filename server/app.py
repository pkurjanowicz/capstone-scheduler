import os
from flask import Flask, render_template
from userAPI import user_api, User, Event
from db_instance import db

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "userdata.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(user_api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()