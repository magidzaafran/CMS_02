"""
The flask application package.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask extensions
db = SQLAlchemy(app)
Session(app)

# Initialize Flask-Login
login = LoginManager(app)
login.login_view = 'login'

# Import views after app is initialized to avoid circular imports
from FlaskWebProject import views, models

@login.user_loader
def load_user(id):
    return models.User.query.get(int(id))
