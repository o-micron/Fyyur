from flask import render_template
from models.shared import db
from models import Artist, Venue


class ArtistRoutes:
    def all():
        return render_template('artists.html')

    def detail():
        return render_template('artist.html')
