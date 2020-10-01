import os

basedir = os.path.dirname(__file__)
basedir = os.path.abspath(basedir)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/shortener'

URL = 'http://127.0.0.1:5000/'
