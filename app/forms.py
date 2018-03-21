from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SelectField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileAllowed, FileField,FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('M', 'Male'), ('F', 'Female')])
    email = StringField('Email', validators = [DataRequired()])
    location = StringField('Location', validators=[InputRequired()])
    bio= TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg','png'])])
     

    
