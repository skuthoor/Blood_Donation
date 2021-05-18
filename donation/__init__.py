from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

global index 
index = 0

global bk
bk = int(0) 

global dt
dt = int(0)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donation.db'
app.config['SECRET_KEY']= '9d47ad7092661e50d62333f0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = "info"

from donation import routes