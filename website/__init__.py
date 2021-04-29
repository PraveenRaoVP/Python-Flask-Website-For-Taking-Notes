# import required modules
from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#set db name
DB_NAME = 'database.db'
db=SQLAlchemy()

#create window
def create_app():
     app = Flask(__name__)
     #secret key
     app.config['SECRET_KEY']="SAIDIMNEVERLACKINGALWAYSPISTOLPACKINGWITHTHEMAUTOMATICSWEGONSENDTHEMTOHEAVEN"
     app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{DB_NAME}"
     db.init_app(app)
     
     from .views import views
     from .auth import auth
     
     create_database(app)
     return app 

#create database
def create_database(app):
     if not path.exists('website/'+DB_NAME):
          db.create_all(app=app)
          
          