from flask import Flask

from model import db
from shortener.routes import short_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    app.register_blueprint(short_blueprint)
    return app
