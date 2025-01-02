## Flask experimentations

This project is a basic exploration in the python Flask framework for personal learning, leveraging various Flask extensions to host the frame of a personal website, and to manage and handle a contact form defensively against potential abuses. 

Additionally it handles mail functionality with Flask-Mail, coordinating with an smtp mail server to direct emails from form to the site owner.

### Environment Configuration

| Variable Name          | Description                                                   | Example Value           |
|------------------------|---------------------------------------------------------------|-------------------------|
| `MAIL_USERNAME`        | Gmail account used for sending emails.                        | `your-email@gmail.com`  |
| `MAIL_PASSWORD`        | Gmail account password for SMTP login.                        | `yourpassword123`       |
| `TESTING_ADDRESS`      | Email address to test receiving emails.                       | `test-recipient@mail.com` |
| `CSRF_SECRET_KEY`      | Generated key to secure against CSRF attacks.                | `randomlyGeneratedKey123` |
| `RECAPTCHA_SITE_KEY`   | Google reCAPTCHA site key, obtained from Google reCAPTCHA setup. | `6Lc...xyz`             |
| `RECAPTCHA_SECRET_KEY` | Google reCAPTCHA secret key, obtained from Google reCAPTCHA setup. | `6Lc...abc`             |