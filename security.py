from flask_login import LoginManager
from flask.ext.hashing import Hashing

from db import db
import models
from models import Users

login_manager = LoginManager()
hashing = Hashing()

login_manager.login_view = "user.login"



@login_manager.user_loader
def load_user(user_id):
    return db.session.query(models.Users).filter(models.Users.id == user_id).first()