from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def reset_database():
    from src.database.models import Student  # noqa
    db.drop_all()
    db.create_all()
