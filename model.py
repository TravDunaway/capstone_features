from enum import unique
import os
from flask_sqlalchemy import SQLAlchemy

#
from __init__ import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#^^

#
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
#^^^




db = SQLAlchemy()
#
class User(db.Model,UserMixin):
# usermixin^
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    # password = db.Column(db.String(255), nullable = False)
    
    #
    password_hash = db.Column(db.String(255), nullable = False)
    #^^
    user_email = db.Column(db.String(255), unique = True, nullable = False)

    times = db.relationship("Time", backref = "user", lazy = True)

    def __init__(self, username, password, user_email):
        self.username = username
        # self.password = password
        #
        self.password_hash = generate_password_hash(password)
        #^^
        self.user_email = user_email

    #
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    #^^
    
    def get_all_choices(self):
        # choices = []
        pass
        # for time in self.times:
        #     for choice in time.choices:
        #         choices.extend(choice)

        # return choices
    
    def get_all_times(self):
        pass
        # times = []

        # for time in self.times:
        #     times.extend(time)

        # return times

    def get_all_users(self):
        # users = []
        pass
        # for user in self.users:
        #     users.extend(user)

        # return users

class Time(db.Model):

    __tablename__ = "times"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    time = db.Column(db.Integer, unique = False, nullable = False)
    current_location = db.Column(db.Integer, unique = False, nullable = False)
    date = db.Column(db.Integer, unique = False, nullable = False)

    choices = db.relationship("Choice", backref = "time", lazy = True)

class Choice(db.Model):

    __tablename__ = "choices"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    time_id = db.Column(db.Integer, db.ForeignKey("times.id"), unique = False,  nullable = False)
    trip_time = db.Column(db.Integer, unique = False,  nullable = False)
    desination = db.Column(db.Integer, unique = False,  nullable = False)
    

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("connected to db...")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    




































# class Signup(db.Model):

#     __tablename__ = "signups"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     user_name_signup = db.Column(db.String(255), unique = True, nullable = False)
#     user_name_signup_email= db.Column(db.String(255), unique = False, nullable = False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
#     remember_me = db.Column(db.Boolean, default = False)

#     logins = db.relationship("Login", backref = "signup", lazy = True)

#     def __init__(self, user_name_signup, user_id):
#         self.user_name_signup = user_name_signup
#         self.user_name_signup_email= user_id

# class Login(db.Model):

#     __tablename__ = "logins"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     user_login_email = db.Column(db.String(255), unique = True, nullable = False)
#     user_login_password = db.Column(db.String(255), unique = False, nullable = True)
#     remember_me = db.Column(db.Boolean, default = False)
#     signup_id = db.Column(db.Integer, db.ForeignKey("signups.id"), nullable = False)

#     sessioninfos = db.relationship("Sessioninfo", backref = "login", lazy = True)

#     def __init__(self, user_login_email, user_login_password, remember_me, signup_id, **kwargs):
#         self.user_login_email = user_login_email
#         self.user_login_password = user_login_password
#         self.remember_me = remember_me
#         self.signup_id = signup_id

#         if "user_login_email" in kwargs:
#             self.user_login_email = kwargs["user_login_email"]

# class Sessioninfo(db.Model):

#     __tablename__ = "sessioninfos"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     login_time = db.Column(db.String(255), unique = False, nullable = False)
#     login_id = db.Column(db.Integer, db.ForeignKey("logins.id"), nullable = False)
#     login_date = db.Column(db.String(255), unique = False, nullable = False)
#     user_choice = db.Column(db.String(255), unique = False, nullable = False)

#     routetimes = db.relationship("Routetime", backref = "sessioninfo", lazy = True)

# class Routetime(db.Model):

#     __tablename__ = "routetimes"

#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     time_given = db.Column(db.String(255), unique = False, nullable = False)
#     session_id = db.Column(db.Integer, db.ForeignKey("sessioninfos.id"), nullable = False)
#     # session_info = db.Column(db.Integer, db.ForeignKey("sessioninfos.id"), nullable = False)






# def connect_to_db(app):
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     db.app = app
#     db.init_app(app)

# if __name__ == "__main__":
#     from flask import Flask
#     app = Flask(__name__)
#     connect_to_db(app)
#     print("Connected to db...")