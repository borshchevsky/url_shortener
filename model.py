from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), nullable=True, unique=True)
    short_url = db.Column(db.String())
    creation_time = db.Column(db.DateTime(), default=datetime.now())
    used = db.Column(db.Integer(), default=0)



