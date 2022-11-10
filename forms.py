from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, email_validator, EqualTo
from model import User


#
class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=255), EqualTo('pass_confirm', message='Passwords must match!')])
    user_email = StringField('Email', validators=[DataRequired(), Length(min=4, max=255), email_validator()])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")
#^^    
    def check_email(self):
        if User.query.filter_by(user_email=self.user_email.data).first():
            print("doesn't work-email")
            raise ValidationError("Email already exists!")
         
        else:
            print("new user info is valid and submitted")
            return True
          
        
    def check_username(self):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Username is taken!")
          
        else:
            return True

class OldUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Log In")

    def check_user_info(self):
        if User.query.filter_by(username=self.username.data, password=self.password.data).first():
            print("Username and password match are good to go.")
            return True
        else:
            print("Username and password don't match")
            return False




















