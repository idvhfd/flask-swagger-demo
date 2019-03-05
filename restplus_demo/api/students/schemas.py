from marshmallow import validate, ValidationError
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema


class StudentSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    city = fields.Str(required=True)
    address = fields.Str(required=True)
    pin = fields.Str(required=True)

    class Meta:
        type_ = 'students'
