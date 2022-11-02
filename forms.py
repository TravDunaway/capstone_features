from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


# class wtforms.validators.Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True,       allow_empty_local=False)


class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=255)])
    user_email = StringField('Email', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")
    
class OldUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=255)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")




















