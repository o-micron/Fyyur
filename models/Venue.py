from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, default="")
    seeking_talent_description = db.Column(db.String, default="")
    website = db.Column(db.String, default="")
    image_link = db.Column(db.String, default="")
    facebook_link = db.Column(db.String, default="")
    children = db.relationship('Show', backref='venue')

    def __repr__(self):
        return f'''<
        Venue id: {self.id},
        creation_date: {self.creation_date},
        name: {self.name},
        genres: {self.genres},
        city: {self.city},
        state: {self.state},
        address: {self.address},
        phone: {self.phone},
        seeking_talent_description: {self.seeking_talent_description},
        website: {self.website},
        image_link: {self.image_link},
        facebook_link: {self.facebook_link}
        >'''
