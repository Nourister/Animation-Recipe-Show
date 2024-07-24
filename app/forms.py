from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from email_validator import validate_email, EmailNotValidError
from .models import User
from flask_wtf.file import FileField, FileRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), Length(min=6), EqualTo('password1')])
    submit = SubmitField('Sign In')

    def validate_username(self, username):
        """Validate if the username exists"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise EmailNotValidError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        try:
            validate_email(email.data)
        except EmailNotValidError as e:
            raise ValueError('Invalid email address')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')