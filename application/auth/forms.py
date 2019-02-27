from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.Length(min=2, max=20)])
    password = PasswordField("Salasana", [validators.Length(min=8, max=20)])

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.Length(min=2, max=20)])
    password = PasswordField("Salasana", [validators.Length(min=8, max=20)])

    class Meta:
        csrf = False
