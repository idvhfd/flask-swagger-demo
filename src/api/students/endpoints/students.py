import logging

from flask import request
from flask_restplus import Resource
from src.api.students.operations import create_student, delete_student, update_student
from src.api.students.serializers import serial_student
from src.api.restplus import api
from src.database.models import Student

log = logging.getLogger(__name__)

ns = api.namespace('students', description='Operations related to students')


@ns.route('/')
class StudentCollection(Resource):
    @api.marshal_with(serial_student)
    def get(self):
        """
        Returns list of all students.
        """
        return Student.query

    @api.expect(serial_student)
    def post(self):
        """
        Creates a new student.
        """
        create_student(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Student not found.')
class StudentItem(Resource):
    @api.marshal_with(serial_student)
    def get(self, id):
        """
        Returns a student.
        """
        return Student.query.filter(Student.id == id).one()

    @api.expect(serial_student)
    @api.response(204, 'Student successfully updated.')
    def put(self, id):
        """
        Updates a student.
        """
        data = request.json
        update_student(id, data)
        return None, 204

    @api.response(204, 'Student successfully deleted.')
    def delete(self, id):
        """
        Deletes a student.
        """
        delete_student(id)
        return None, 204
