import os

from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_folder = os.path.join(BASE_DIR, 'web/static')
template_folder = os.path.join(BASE_DIR, 'web/templates')

class Config(object):
    DEBUG = False
    TESTING = False


class RealConfig(Config):
    pass


class StageConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True
    TESTING = True

app = Flask(
    __name__,
    static_folder=static_folder,
    template_folder=template_folder,
    static_url_path='/static'
)
# if 'SERVER' in os.environ:
#     if os.environ['SERVER'] == 'REAL':
#         app.config.from_object('config.RealConfig')
#     elif os.environ['SERVER'] == 'STAGE':
#         app.config.from_object('config.StageConfig')
# else:
app.config.from_object(DevConfig)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/scss', 'static/css', '/static/css')
})


@app.route('/')
def index():
    message = "Hello Flask!"
    return render_template('index.html', message=message)


@app.route('/photo')
def photo():
    message = "Hello Flask!"
    return render_template('photo.html', message=message)


if __name__ == '__main__':
    app.run()
