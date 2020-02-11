from flask import render_template
from models.Artist import Artist


class ArtistRouter:
    def all():
        return render_template('artists.html', data={
            'artists': Artist.query.all()
        })

    def detail(artist_id):
        return render_template('artist.html', data={
            'artist': Artist.query.get(artist_id)
        })
