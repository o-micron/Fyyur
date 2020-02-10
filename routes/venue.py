from flask import render_template
from models.shared import db
from models import Artist, Venue


class VenueRoutes:
    def all():
        return render_template('venues.html')

    def detail():
        return render_template('venue.html')
