from flask import Blueprint, redirect, request
from marshmallow import ValidationError

from model import Url, db
from schemas import ShortSchema
from shortener.config import URL

short_blueprint = Blueprint('short', __name__)


@short_blueprint.route('/', methods=['POST'])
def return_short_url():
    json = request.json
    if not json:
        return {'response': 'no data'}

    schema = ShortSchema()

    try:
        data = schema.load(json)
    except ValidationError as e:
        return e.messages

    exists = Url.query.filter_by(url=data.url).first()
    if not exists:
        db.session.add(data)
        db.session.commit()
        return {'short_url': f'{URL}{data.short_url}'}
    else:
        return {'short_url': f'{URL}{exists.short_url}'}


@short_blueprint.route('/<short_url>')
def redirect_from_short(short_url):
    short = Url.query.filter_by(short_url=short_url).first()
    if short:
        Url.query.filter_by(id=short.id).update({'used': short.used + 1})
        db.session.commit()
        return redirect(short.url)
    else:
        return 'No such short url'


@short_blueprint.route('/statistics/<short_url>')
def get_stats(short_url):
    short = Url.query.filter_by(short_url=short_url).first()
    if short:
        return {'count': short.used}
    else:
        return "No such short url"
