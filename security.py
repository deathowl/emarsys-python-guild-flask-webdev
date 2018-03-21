from flask_login import LoginManager
from flask.ext.hashing import Hashing

from db import db
import models
from models import Users
from settings import ALLOWED_EXTENSIONS
login_manager = LoginManager()
hashing = Hashing()

login_manager.login_view = "user.login"



@login_manager.user_loader
def load_user(user_id):
    return db.session.query(models.Users).filter(models.Users.id == user_id).first()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS