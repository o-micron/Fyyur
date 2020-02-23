from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.shared import db, pending_notifications
from sqlalchemy import func, desc
from utils.parser import parse_error

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
            pending_notifications.append({"title": "Success", "body": "Created a new artist successfully"})
            return True
        except Exception as ex:
            self.rollback()
            status = parse_error(ex.orig)
            pending_notifications.append({"title": "Failure", "body": status})
            return False

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as ex:
            self.rollback()
            return ex

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as ex:
            self.rollback()
            return ex

    def get_by_name(name):
        try:
            artist = Artist.query.filter(Artist.name == name).one()
            return artist
        except Exception:
            return None

    def create_from_form(form):
        name = form.name.data
        genres = ','.join(form.genres.data)
        city = form.city.data
        state = form.state.data
        phone = form.phone.data
        website = form.website.data
        image_link = form.image_link.data
        facebook_link = form.facebook_link.data
        return Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)

    def search_for(text):
        return Artist.query.filter(Artist.name.like('%' + text + '%')).order_by('name').all()

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