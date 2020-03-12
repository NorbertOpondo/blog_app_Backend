from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b92c9faa583a03dcfaa38571ca3fd9e6'
#creating and setting up the location of our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

#creating a database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login is the function name of the route, Same as what would be passed in the url_for() function

#This will style the login message at the top of the loginForm, will give it the pre defined bootsrap class .info
login_manager.login_message_category = 'info' 

from flaskblog import routes