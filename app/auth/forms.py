''''''
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField, SubmitField

class SigninForm(FlaskForm):
    ''''''
    email = EmailField()
    password = PasswordField()
    submit = SubmitField()

class SignupForm(FlaskForm):
    ''''''
    email = EmailField()
    password = PasswordField()
    submit = SubmitField()
