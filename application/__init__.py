from flask import Flask
from flask_cors import CORS
#For persistent storage
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_heroku import Heroku
import os

#create the Flask app
app = Flask(__name__)
#CORS(app)
# load configuration from config.cfg
app.config.from_pyfile('config.cfg')
# instantiate the Heroku object before db
heroku = Heroku(app)
# instantiate SQLAlchemy to handle db process
db = SQLAlchemy(app)

from application import routes


