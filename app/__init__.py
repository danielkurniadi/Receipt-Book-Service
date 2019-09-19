from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
flask_app = Flask(__name__)

# Configurations
flask_app.config.from_object('config.flask_config')
