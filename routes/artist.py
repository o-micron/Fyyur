import json
from flask import render_template, url_for, redirect, request
from models.Artist import Artist
from models.shared import db


class ArtistRouter:
    def view_all():
        return render_template('artists.html', data={
            'artists': Artist.query.all()
        })

    def view_detail(artist_id):
        return render_template('artist.html', data={
            'artist': Artist.query.get(artist_id)
        })

    def create():
        data = json.loads(request.data)
        name = data['name']
        city = data['city']
        state = data['state']
        phone = data['phone']
        genres = ','.join(data['genres'])
        facebook_link = data['facebook_link']
        artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('view_all_artists'))
