from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from flask_wtf.file import FileField


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service)',
                              [validators.DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class UploadForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    file = FileField()
