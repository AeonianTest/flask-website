from flask_wtf import FlaskForm, RecaptchaField #import the flask-wtf form stuff
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class MailForm(FlaskForm): #define a form
    name = StringField("Name", validators=[DataRequired()]) #The fields of the form, and their validations
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = StringField("Message", validators=[DataRequired()])
    recaptcha = RecaptchaField() #v2 recaptcha field
    submit = SubmitField("Send") #Submission button