import os
from flask import Flask
from security import login_manager, hashing
import models
from db import db
import settings
from flask_admin import Admin
from adminviews import MyModelView
from controllers import home, user
from flask_wtf.csrf import CSRFProtect


def setup_app():
    app = Flask(__name__)
    app.testing = settings.TEST_MODE
    app.secret_key = settings.SECRET
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.ALCHEMY_URL
    db.init_app(app)
    admin = Admin(app, name='Porghub Admin', template_mode='bootstrap3')
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    hashing.init_app(app)
    admin.add_view(MyModelView(models.Users, db.session,
                            column_list=['id', 'name', "description", "is_active", "is_admin"],
                            search_fields=['username'],
                            form_columns=['id', 'name', "description", "is_active", "is_admin"]))

    admin.add_view(
        MyModelView(models.Comments, db.session, form_columns=['user', 'video', 'text']))
    admin.add_view(
        MyModelView(models.Videos, db.session, form_columns=['user', 'title'],
                    search_fields=['title']))
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(user, url_prefix='/user')

    return app



application = setup_app()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3031))
    application.run('0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', False))