from flask import Flask, render_template, request, redirect, make_response, jsonify #Import the Flask modules
from flask_mail import Mail, Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from dotenv import load_dotenv #import misc modules

import os



app = Flask(__name__) #setting up the app

limiter = Limiter( #Initialize the rate limiter object, use for form
    get_remote_address,  #Get user ip
    app=app, 
    default_limits=["200 per minute"], #Global limits for general usage
    storage_uri="memory://" #For a prod app might have to be changed.
)

#gmail smtp server setup with env vars
load_dotenv()
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #using gmail for smtp solution
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME") #Get the gmail account from .env
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app) #Set up mail service

@app.route('/') #Render the pages
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact") #HAVE TO SET UP FORM CHECKS TO PREVENT SPAM
def contact():
    return render_template("contact.html")

@app.route("/send_email", methods=["POST"]) #WIP for rate limiting form validation captcha etc
@limiter.limit('20 per hour')
def send_email():
    #Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    try: #Try to send message
        msg = Message( #Compose the message instance
            subject=f"Message from {name}",
            recipients=[os.getenv("TESTING_ADDRESS")],
            body=f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"
        )

        mail.send(msg) #Send the message
        return redirect('/contact')
    except Exception as e: #Catch error
        return f"Failed to send email: {e}"
    
@app.errorhandler(429) #Handle rate limit response
def ratelimit_handler(e):
    return make_response(
            jsonify(error=f"ratelimit exceeded {e.description}")
            , 429
    )

if __name__ == '__main__': #If run as main python file, start the application
    app.run(debug=True)