from flask import Flask
import joblib
#For persistent storage
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_heroku import Heroku
import os

#create the Flask app
app = Flask(__name__)

if "TESTING" in os.environ:
    app.config.from_envvar('TESTING')
    print("Using config for TESTING")
elif "DEVELOPMENT" in os.environ:
    app.config.from_envvar('DEVELOPMENT')
    print("Using config for DEVELOPMENT")
else:
    app.config.from_pyfile('config_dply.cfg')
    # app.config.from_pyfile('config_test.cfg')
    print("Using config for deployment")

# load configuration from config.cfg
# app.config.from_pyfile('config.cfg')
# instantiate the Heroku object before db
heroku = Heroku(app)
# instantiate SQLAlchemy to handle db process
db = SQLAlchemy(app)

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'

#     db.init_app(app)

#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     from .models import User

#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app

#AI model file
joblib_file = "./application/static/joblib_model.pkl"
# Load from file
ai_model = joblib.load(joblib_file)


#run the file routes.py
from application import routes
