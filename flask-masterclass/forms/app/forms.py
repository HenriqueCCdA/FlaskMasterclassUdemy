from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import EmailField
from wtforms.fields import PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField("Senha", validators=[
       Length(3, 6, "O campo deve conter entre 3 à 6 caracters.")
    ])
    remember  = BooleanField('Permanecer Conectado')
    submit = SubmitField('Logar')


class RegisterForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired("O campo é obrigatório")])
    email = EmailField('Email', validators=[Email()])
    password = PasswordField("Senha", validators=[
       Length(3, 6, "O campo deve conter entre 3 à 6 caracters.")
    ])
    submit = SubmitField('Cadastrar')
