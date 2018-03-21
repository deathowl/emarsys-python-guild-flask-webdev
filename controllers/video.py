import os
from flask import request, session, redirect, render_template, flash, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

import settings
from db import db
from flask.blueprints import Blueprint

from forms import UploadForm
from models import Videos

from security import allowed_file


video = Blueprint('video', __name__,
                 template_folder='templates',
                 static_folder='static')

@video.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    form = UploadForm(request.form)
    form.validate()
    print(form.errors)
    if request.method == "POST" and form.validate():
        # check if the post request has the file part
        # if user does not select file, browser also
        # submit a empty part without filename
        f = form.file.data
        filename = secure_filename(f.filename)
        if f and allowed_file(filename):
            f.save((os.path.join(settings.UPLOAD_FOLDER, filename)))
            video = Videos()
            video.path = filename
            video.title = form.title
            video.description = form.description

            return redirect(url_for('video.view',
                                    id=id))
    else:
        return render_template("upload.html", form=form)