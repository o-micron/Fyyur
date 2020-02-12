from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    genres = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(120), default="")
    state = db.Column(db.String(120), default="")
    address = db.Column(db.String(120), default="")
    phone = db.Column(db.String(120), default="")
    seeking_talent_description = db.Column(db.String(300), default="")
    website = db.Column(db.String, default="")
    image_link = db.Column(db.String, default="")
    facebook_link = db.Column(db.String, default="")
    children = db.relationship('Show', backref='venue')

    def __repr__(self):
        return f'''<
        Venue id: {self.id}, 
        name: {self.name},
        genres: {self.genres},
        city: {self.city},
        state: {self.state},
        address: {self.address},
        phone: {self.phone},
        website: {self.website},
        image_link: {self.image_link},
        facebook_link: {self.facebook_link},
        seeking_talent_description: {self.seeking_talent_description}
        >'''
