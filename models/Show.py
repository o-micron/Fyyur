from flask_sqlalchemy import SQLAlchemy
from models.shared import db


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Date, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

    def __repr__(self):
        return f'''
        <Show id: {self.id},
        name: {self.name},
        start_time: {self.date},
        artist_id: {self.artist_id}>
        venue_id: {self.venue_id},
        '''
