from src.database import db
from src.database.models import Student


def create_student(data):
    name = data.get('name')
    city = data.get('city')
    address = data.get('address')
    pin = data.get('pin')

    student = Student(name, city, address, pin)

    db.session.add(student)
    db.session.commit()


def update_student(student_id, data):
    student = Student.query.filter(Student.id == student_id).one()

    student.name = data.get('name')
    student.city = data.get('city')
    student.address = data.get('address')
    student.pin = data.get('pin')

    db.session.add(student)
    db.session.commit()


def delete_student(student_id):
    student = Student.query.filter(Student.id == student_id).one()
    db.session.delete(student)
    db.session.commit()

