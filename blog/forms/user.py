from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()],)
    first_name = StringField("First Name")
    last_name = StringField("Last name")
    email = StringField("E-mail", [validators.DataRequired(), validators.Email()], filters=[lambda data: data and data.lower()], )
    


class RegistrationForm(UserBaseForm):
    password = PasswordField("Password", [validators.DataRequired(), validators.EqualTo("confirm_password", message="Passwords must match")])
    confirm_password = PasswordField("Repeat Password", [validators.DataRequired()])
    submit = SubmitField("Register")