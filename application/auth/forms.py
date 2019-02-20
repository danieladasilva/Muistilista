from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Käyttäjä", [validators.Length(min=2, max=64)])
    password = PasswordField("Salasana", [validators.Length(min=2, max=128)])

    class Meta:
        csrf = False
