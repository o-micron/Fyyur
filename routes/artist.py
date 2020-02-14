import json
from flask import render_template, url_for, redirect, request
from models.Artist import Artist
from forms.Artist import ArtistForm
from models.Show import Show
from models.shared import db


class ArtistRouter:
    def view_all():
        if request.method == 'POST':
            searchQuery = request.form.get('searchQuery')
            searchQuery = searchQuery.lstrip()
            if searchQuery:
                return render_template('artists.html', data={
                    'artists': Artist.query.filter(Artist.name.like('%' + searchQuery + '%')).all(),
                    'searchQuery': searchQuery
                })
            else:
                return render_template('artists.html', data={
                    'artists': Artist.query.all(),
                    'searchQuery': ''
                })
        else:
            return render_template('artists.html', data={
                'artists': Artist.query.all(),
                'searchQuery': ''
            })

    def view_detail(artist_id):
        return render_template('artist.html', data={
            'artist': Artist.query.get(artist_id),
            'shows': Show.query.filter(Show.artist_id == artist_id)
        })

    def create():
        if request.method == 'POST':
            name = request.form.get('name')
            city = request.form.get('city')
            state = request.form.get('state')
            phone = request.form.get('phone')
            genres = ','.join(request.form.get('genres'))
            facebook_link = request.form.get('facebook_link')
            artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
            db.session.add(artist)
            db.session.commit()
            return redirect(url_for('view_all_artists'))
        elif request.method == 'GET':
            form = ArtistForm()
            return render_template('forms/create_artist.html', form=form)
