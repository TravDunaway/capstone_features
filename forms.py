from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
from model import User

# class wtforms.validators.Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True,       allow_empty_local=False)


class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=255)])
    user_email = StringField('Email', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")
    
    def check_email(self,):
        if User.query.filter_by(user_email=self.user_email.data).first():
            print("doesn't work-email")
            return False
        else:
            print("new user info is valid and submitted")
            return True
            # raise ValidationError('Your email has already been registered!')

        
    def check_username(self):
        if User.query.filter_by(username=self.username.data).first():
            return False
        else:
            return True

class OldUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")

    def check_user_info(self):
        if User.query.filter_by(username=self.username.data, password=self.password.data).first():
            print("Username and password match are good to go.")
            return True
        else:
            print("Username and password don't match")
            return False




















