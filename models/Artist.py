from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.shared import db
from sqlalchemy import func, desc

class Artist(db.Model):
    __tablename__ = 'artists'
    COUNT_PER_PAGE = 8

    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, default="")
    seeking_venue_description = db.Column(db.String, default="")
    website = db.Column(db.String, default="")
    image_link = db.Column(db.String, default="")
    facebook_link = db.Column(db.String, default="")
    children = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'''<
        Artist id: {self.id},
        creation_date: {self.creation_date},
        name: {self.name}, 
        genres: {self.genres},
        city: {self.city}, 
        state: {self.state}, 
        phone: {self.phone},
        seeking_venue_description: {self.seeking_venue_description},
        website: {self.website},
        image_link: {self.image_link}, 
        facebook_link: {self.facebook_link}
        >'''

    def rollback(self):
        db.session.rollback()

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as ex:
            rollback()
            return ex

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as ex:
            rollback()
            return ex

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as ex:
            rollback()
            return ex

    def fetch_recent(cpp:int=COUNT_PER_PAGE):
        data = Artist.query.order_by(Artist.creation_date.desc()).all()
        if(len(data) > cpp):
            return data[:cpp]
        else:
            return data

    def fetch_page(page:int, cpp:int=COUNT_PER_PAGE):
        if(page >= 1):
            return Artist.query.order_by(Artist.name.asc()).paginate(page, cpp, False).items
        else:
            return Artist.query.order_by(Artist.name.asc()).all()

    def fetch_top(cpp:int=COUNT_PER_PAGE):
        data = Artist.query.join(Artist.children).group_by(Artist.id).order_by(desc(func.count())).all()
        if(len(data) > cpp):
            return data[:cpp]
        else:
            return data