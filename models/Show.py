from flask_sqlalchemy import SQLAlchemy
from models.Artist import Artist
from models.Venue import Venue
from models.shared import db, pending_notifications
from utils.parser import parse_error


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint(start_time, artist_id, venue_id),
    )
    
    def __repr__(self):
        return f'''
        <Show id: {self.id},
        name: {self.name},
        start_time: {self.date},
        artist_id: {self.artist_id}>
        venue_id: {self.venue_id},
        '''

    def rollback(self):
        db.session.rollback()

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            pending_notifications.append({"title": "Success", "body": "Created a new show successfully"})
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

    def create_from_form(form):
        artist = Artist.get_by_name(form.artist_id.data)
        venue = Venue.get_by_name(form.venue_id.data)
        start_time = form.start_time.data
        if artist is None:
            form.artist_id.errors.append('Please enter a valid artist name')
        if venue is None:
            form.venue_id.errors.append('Please enter a valid venue name')
        if artist is not None and venue is not None:
            return (form, Show(artist_id=artist.id, venue_id=venue.id, start_time=start_time))
        else:
            return (form, None)