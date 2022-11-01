from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class SignupForm(FlaskForm):
    user_signup_email = StringField('User Name', validators=[DataRequired(), Length(min=4, max=255)])
    user_signup_password = StringField('User Password', validators=[DataRequired(), Length(min=4, max=255)])
    remember_me = BooleanField("Remember Me?")
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
   user_login_email = StringField('User Name', validators=[DataRequired(), Length(min=4, max=255)])
   user_login_password = StringField('User Password', validators=[DataRequired(), Length(min=4, max=255)])
   remember_me = BooleanField("Remember Me?")
   submit = SubmitField("Login")


