import os
from flask import Flask, render_template, Blueprint
from userAPI import user_api, User, Event
from emailAPI import email_api
from db_instance import db


"""
are these .env variables below...and look at that get command. I'm not 
sure you're supposed to post code like that in python at all
"""

FB_CLIENT_ID = os.environ.get("FB_CLIENT_ID")
FB_CLIENT_SECRET = os.environ.get("FB_CLIENT_SECRET")
FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"
USERINFO_URL = "https://app.simplelogin.io/oauth2/userinfo"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


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
    app.register_blueprint(email_api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

