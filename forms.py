from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators


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