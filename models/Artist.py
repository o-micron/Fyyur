from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Artist id: {self.id}, name: {self.name}>'
