from flask import Flask, render_template, request, redirect #Import the modules
from flask_mail import Mail, Message
from dotenv import load_dotenv

import os

app = Flask(__name__) #setting up the app. Also import from .env
load_dotenv()

#gmail smtp server setup with env vars
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
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

if __name__ == '__main__': #If run as main python file, start the application
    app.run(debug=True)