from flask_restplus import fields
from restplus_demo.api.restplus import api

serial_student = api.model('Student', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a student'),
    'name': fields.String(required=True, description='Student name'),
    'city': fields.String(required=True, description='Student city'),
    'address': fields.String(required=True, description='Student address'),
    'pin': fields.Integer(required=True, description='Student pin'),
})
