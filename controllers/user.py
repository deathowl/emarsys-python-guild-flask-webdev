
from flask import request, session, redirect, render_template, flash
from flask_login import login_user, logout_user

import models
import settings
from db import db
from flask.blueprints import Blueprint
from models import Users
from security import hashing
from forms import RegistrationForm, LoginForm

user = Blueprint('user', __name__,
                 template_folder='templates',
                 static_folder='static')




@user.route("/signup", methods=["GET", "POST"])
def register():

    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = hashing.hash_value(form.password.data, settings.SECRET)

        already_exists = db.session.query(models.Users).filter(models.Users.name==username).count()

        if already_exists:
            flash("That username is already taken, please choose another")
            return render_template('register.html', form=form)

        else:
            new_user = models.Users()
            new_user.name = username
            new_user.password = password
            new_user.is_admin = False
            db.session.add(new_user)
            db.session.commit()
            return redirect('//')
    else:

        return render_template("register.html", form=form)


@user.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        print(form.password.data)
        user = db.session.query(models.Users).filter(models.Users.name == username).first()

        if not user or user and not hashing.check_value(user.password, password, settings.SECRET):
            flash("Failed to log you in with these credentials")
            return render_template("login.html", form=form)

        else:
            #login
            login_user(user)
            return redirect('//')
    else:

        return render_template("login.html", form=form)



@user.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect('/')
