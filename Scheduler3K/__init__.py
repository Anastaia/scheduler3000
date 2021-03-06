from os.path import join, dirname, realpath
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/files/')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f106a85651d73990e22af513b9dbfa24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'


from Scheduler3K import routes
