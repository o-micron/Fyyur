import json
from flask import render_template, url_for, redirect, request, flash
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
        form = ArtistForm()
        print("\n\nForm: ")
        print(form.name.data)
        print(form.city.data)
        print(form.state.data)
        print(form.phone.data)
        print(form.genres.data)
        print(form.facebook_link.data)
        print("\n\n")
        if request.method == 'POST' and form.validate_on_submit():
            name = request.form.name.data
            city = request.form.city.data
            state = request.form.state.data
            phone = request.form.phone.data
            genres = request.form.genres.data
            facebook_link = request.form.facebook_link.data
            artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
            db.session.add(artist)
            db.session.commit()
            flash('successfully created a new artist')
            return redirect(url_for('view_all_artists'))
        else:
            return render_template('forms/create_artist.html', form=form)
