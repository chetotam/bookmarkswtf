''''''
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField, SubmitField

class LoginForm(FlaskForm):
    ''''''
    email = EmailField()
    password = PasswordField()
    submit = SubmitField()
