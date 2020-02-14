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
        form = ArtistForm(request.form)
        if request.method == 'POST' and form.validate():
            print("\n\nForm: ")
            print(form.name.data)
            print(form.city.data)
            print(form.state.data)
            print(form.phone.data)
            print(form.genres.data)
            print(form.facebook_link.data)
            print("\n\n")
            name = form.name.data
            city = form.city.data
            state = form.state.data
            phone = form.phone.data
            genres = ','.join(form.genres.data)
            facebook_link = form.facebook_link.data
            artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
            db.session.add(artist)
            db.session.commit()
            flash('successfully created a new artist')
            return redirect(url_for('view_all_artists'))
        return render_template('forms/create_artist.html', form=form)
