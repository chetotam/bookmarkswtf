from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.fields.simple import StringField, SubmitField

class AddBookmarkForm(FlaskForm):
    ''''''
    url = URLField()
    title = StringField()
    description = StringField()
    submit = SubmitField()
