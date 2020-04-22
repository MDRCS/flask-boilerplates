import os
from webapp import create_app
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


""""
The make_celery function wraps every call to each Celery task in a Python with block.
This makes sure that every call to any Flask extension will work as it is working with our app.
Also, make sure not to name the Flask app instance app, as Celery tries to import any object named app
or celery as the Celery application instance.
So naming your Flask object app will cause Celery to try to use it as a Celery object.
"""

env = os.environ.get('WEBAPP_ENV', 'dev')
flask_app = create_app('config.%sConfig' % env.capitalize())

celery = make_celery(flask_app)
