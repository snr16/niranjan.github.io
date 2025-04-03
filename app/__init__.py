from flask import Flask
from flask_mail import Mail
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    # Email configuration
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', True)
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'your-email@gmail.com')

    # Initialize Flask-Mail
    mail = Mail(app)

    # Import and register blueprints after app creation
    from .routes import main
    app.register_blueprint(main)
    
    return app, mail

# If this file is run directly, create and run the app
if __name__ == '__main__':
    create_app() 