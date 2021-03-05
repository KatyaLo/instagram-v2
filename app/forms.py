from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	login = StringField('Номер телефона, имя пользователя или эл. адрес', validators=[DataRequired()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	submit = SubmitField('Войти')
