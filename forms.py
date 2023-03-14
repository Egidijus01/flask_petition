from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):

    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavarde', [DataRequired()])
    komentaras = StringField('Komentaras')


    submit = SubmitField('Submit')