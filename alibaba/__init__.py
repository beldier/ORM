from flask import Flask 
from flask_sqlalchemy import SQLAlchemy,event
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'efc4e24ad0c31dd35924175a2adc5958'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:walkiria@localhost:5432/orm4'




db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager = LoginManager (app)
login_manager.login_view= 'login'
login_manager.login_message_category = 'info'
from alibaba import routes