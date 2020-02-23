from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.shared import db, pending_notifications
from sqlalchemy import func, desc, asc
from utils.parser import parse_error

class Venue(db.Model):
    __tablename__ = 'venues'
    COUNT_PER_PAGE = 8

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

    def rollback(self):
        db.session.rollback()

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            pending_notifications.append({"title": "Success", "body": "Created a new venue successfully"})
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
            venue = Venue.query.filter(Venue.name == name).one()
            return venue
        except Exception:
            return None

    def create_from_form(form):
        name = form.name.data
        city = form.city.data
        state = form.state.data
        address = form.address.data
        phone = form.phone.data
        genres = ','.join(form.genres.data)
        facebook_link = form.facebook_link.data
        return Venue(name=name, city=city, state=state, phone=phone, address=address, genres=genres, facebook_link=facebook_link)

    def search_for(text):
        return Venue.query.filter(Venue.name.like('%' + text + '%')).order_by('name').all()

    def fetch_recent(cpp:int=COUNT_PER_PAGE):
        data = Venue.query.order_by(Venue.creation_date.desc()).all()
        if(len(data) > cpp):
            return data[:cpp]
        else:
            return data

    def fetch_page(page:int, cpp:int=COUNT_PER_PAGE):
        if(page >= 1):
            return Venue.query.order_by(Venue.name.asc()).paginate(page, cpp, False).items
        else:
            return Venue.query.order_by(Venue.name.asc()).all()

    def fetch_top(cpp:int=COUNT_PER_PAGE):
        data = Venue.query.join(Venue.children).group_by(Venue.id).order_by(desc(func.count())).all()
        if(len(data) > cpp):
            return data[:cpp]
        else:
            return data

    def group_by_location():
        data = Venue.query.group_by(Venue.id, Venue.state, Venue.city).order_by(Venue.state, Venue.city, Venue.name).all()
        return data