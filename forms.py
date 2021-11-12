from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length,  EqualTo
 
class LoginForm(FlaskForm):
	email = StringField("Email: ", validators=[Email("Некорректный email")])
	psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
	remember = BooleanField("Запомнить", default = False)
	submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
	user_name = StringField("Имя: ", validators=[Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")])
	user_email = StringField("Email: ", validators=[Email("Некорректный email")])
	user_psw = PasswordField("Пароль: ", validators=[DataRequired(),Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
 
	user_psw2 = PasswordField("Повтор пароля: ", validators=[DataRequired(), EqualTo('psw', message="Пароли не совпадают")])
	submit = SubmitField("Регистрация")