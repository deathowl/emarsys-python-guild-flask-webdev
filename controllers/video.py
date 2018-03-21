from flask import request, session, redirect, render_template, flash
from flask_login import login_required

import settings
from db import db
from flask.blueprints import Blueprint
from models import Videos

video = Blueprint('video', __name__,
                 template_folder='templates',
                 static_folder='static')

@video.route("/upload")
@login_required
def upload():
    return redirect("/lofaszanyad")
