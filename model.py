from enum import unique
import os
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)

    signups = db.relationship("Signup", backref = "user", lazy = True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # def get_all_logins(self):
    #     logins = []

    #     for signup in self.signups:
    #         for login in signup.logins:
    #             logins.append(login)

    #     return logins

class Signup(db.Model):

    __tablename__ = "signups"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name_signup = db.Column(db.String(255), unique = True, nullable = False)
    user_name_signup_email= db.Column(db.String(255), unique = False, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    remember_me = db.Column(db.Boolean, default = False)

    logins = db.relationship("login", backref = "signup", lazy = True)

    def __init__(self, user_name_signup, user_id):
        self.user_name_signup = user_name_signup
        self.user_name_signup_email= user_id

class Login(db.Model):

    __tablename__ = "logins"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_login_email = db.Column(db.String(255), unique = True, nullable = False)
    user_login_password = db.Column(db.String(255), unique = False, nullable = True)
    remember_me = db.Column(db.Boolean, default = False)
    signup_id = db.Column(db.Integer, db.ForeignKey("signups.id"), nullable = False)

    # def __init__(self, user_login_email, remember_me, signup_id, **kwargs):
    #     self.user_login_email = user_login_email
    #     self.remember_me = remember_me
    #     self.signup_id = signup_id

    #     if "user_login_email" in kwargs:
    #         self.user_login_email = kwargs["user_login_email"]

class Sessioninfo(db.Model):

    __tablename__ = "sessioninfos"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    login_time = db.Column(db.String(255), unique = False, nullable = False)
    login_id = db.Column(db.Integer, db.ForeignKey("logins.id"), nullable = False)
    login_date = db.Column(db.String(255), unique = False, nullable = False)
    user_choice = db.Column(db.String(255), unique = False, nullable = False)

class Routetime(db.Model):

    __tablename__ = "routetimes"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    time_given = db.Column(db.String(255), unique = False, nullable = False)
    session_id = db.Column(db.Integer, db.ForeignKey("sessioninfos.id"), nullable = False)
    # session_info = db.Column(db.Integer, db.ForeignKey("sessioninfos.id"), nullable = False)






def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")