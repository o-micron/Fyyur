from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    genres = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(120), default="")
    state = db.Column(db.String(120), default="")
    phone = db.Column(db.String(120), default="")
    seeking_venue_description = db.Column(db.String(300), default="")
    website = db.Column(db.String, default="")
    image_link = db.Column(db.String, default="")
    facebook_link = db.Column(db.String, default="")
    children = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'''<
        Artist id: {self.id}, 
        name: {self.name}, 
        genres: {self.genres}
        city: {self.city}, 
        state: {self.state}, 
        phone: {self.phone},
        website: {self.website},
        seeking_venue_description: {self.seeking_venue_description},
        image_link: {self.image_link}, 
        facebook_link: {self.facebook_link}
        >'''
