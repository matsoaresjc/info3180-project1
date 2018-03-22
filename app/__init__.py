from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pfeqceengryjol:cbc83af95e2161c96f93f95c177423f6f7cbeb2c20a59ef7b3f743ac4fbc64e0@ec2-50-19-88-36.compute-1.amazonaws.com:5432/d96rdv501f7vnc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER = './app/static/uploads'
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
