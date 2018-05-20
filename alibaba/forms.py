from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from alibaba.models import Usuario
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
	username= StringField('Username',
							validators=[DataRequired(), Length(min=5,max=20)])
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password= PasswordField('Password',validators=[DataRequired() ])
	confirm_password = PasswordField('Confirm Password',
										validators=[DataRequired(),EqualTo('password') ])
	submit= SubmitField('Sign Up')

	def validate_username(self, username):
		user =Usuario.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Ese nombre de usuario ya existe')

class LoginForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	password = PasswordField('Password',validators=[DataRequired() ])
	remember = BooleanField('Remember Me')
	submit= SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username= StringField('Username',
							validators=[DataRequired(), Length(min=5,max=20)])
	email = StringField('Email',
							validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
	submit= SubmitField('Update')


	def validate_username(self, username):
		if username.data != current_user.username: 
			user =Usuario.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Ese nombre de usuario ya existe')
class ItemForm(FlaskForm):
	title= StringField('Titulo', validators=[DataRequired()])
	precio= StringField('Precio', validators=[DataRequired()])
	content= TextAreaField('Descripcion',validators=[DataRequired()])
	submit= SubmitField('Vender')
