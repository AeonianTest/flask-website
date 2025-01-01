from flask_wtf import FlaskForm, RecaptchaField #import the flask-wtf form stuff
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class MailForm(FlaskForm): #define a form
    name = StringField( #The fields of the form, and their validations
        "Name", 
        validators=[DataRequired(message="Name is required")] #message is the returned error message in case of bad input
    ) #Due to html5 forms, I think the DataRequired will not actually show before inbuilt required catchs it
    email = StringField(
        "Email", 
        validators=[DataRequired(message="Email is required"), Email(message="Invalid email format")]
    )
    message = StringField(
        "Message", 
        validators=[DataRequired(message="Message is required")]
    )
    recaptcha = RecaptchaField() #v2 recaptcha field
    submit = SubmitField("Send") #Submission button