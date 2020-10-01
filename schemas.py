from marshmallow import Schema, fields, post_load, validate

from model import Url
from utils import generate_short_url


class ShortSchema(Schema):
    url = fields.String(validate=validate.URL())
    short_url = fields.String()
    creation_time = fields.DateTime()
    used = fields.Integer()

    @post_load
    def make_obj(self, data, **kwargs):
        data['short_url'] = generate_short_url()
        return Url(**data)
