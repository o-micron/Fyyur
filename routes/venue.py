from flask import render_template
from models.shared import db
from models.Venue import Venue


class VenueRoutes:
    def all():
        return render_template('venues.html', data={
            'venues': Venue.query.all()
        })

    def detail(venue_id):
        return render_template('venue.html', data={
            'venue': Venue.query.filter_by(id=venue_id)
        })
