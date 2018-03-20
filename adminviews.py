from flask_admin.contrib.sqla import ModelView

import settings


class MyModelView(ModelView):

    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(MyModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self, *args, **kwargs):
        if settings.TEST_MODE:
            return True

        return True

