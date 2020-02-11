from flask import render_template
from models.shared import db
from models.Venue import Venue


class VenueRouter:
    def all():
        return render_template('venues.html', data={
            'venues': Venue.query.all()
        })

    def detail(venue_id):
        return render_template('venue.html', data={
            'venue': Venue.query.get(venue_id)
        })
