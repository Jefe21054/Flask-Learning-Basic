from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username = StringField('Nombre: ',validators=[DataRequired(message='Ingresa tu nombre')])
    password = PasswordField('Clave: ',validators=[DataRequired(message='Ingresa tu clave'),Length(min=4,max=16)])
    submit = SubmitField('Enviar')