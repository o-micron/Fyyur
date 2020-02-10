from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Show id: {self.id}, name: {self.name}>'
