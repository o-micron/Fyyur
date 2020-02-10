from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Venue id: {self.id}, name: {self.name}>'
