import json
from flask import render_template, url_for, redirect, request, flash
from models.Artist import Artist
from forms.Artist import ArtistForm
from models.Show import Show
from models.shared import db, pending_notifications


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
            notifications = [] + pending_notifications
            pending_notifications.clear()
            return render_template('artists.html', data={
                'artists': Artist.query.all(),
                'searchQuery': ''
            }, notifications=notifications)

    def view_detail(artist_id):
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('artist.html', data={
            'artist': Artist.query.get(artist_id),
            'shows': Show.query.filter(Show.artist_id == artist_id)
        }, notifications=notifications)

    def create():
        form = ArtistForm(request.form)
        if form.validate_on_submit():
            name = form.name.data
            genres = ','.join(form.genres.data)
            city = form.city.data
            state = form.state.data
            phone = form.phone.data
            website = form.website.data
            image_link = form.image_link.data
            facebook_link = form.facebook_link.data
            artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
            db.session.add(artist)
            try:
                db.session.commit()
                pending_notifications.append({"title": "Success", "body": "Created a new artist successfully"})
                flash("Sucess.")
                return redirect(url_for('view_all_artists'))
            except Exception:
                db.session.rollback()
                pending_notifications.append({"title": "Failure", "body": "Invalid Data, Couldn't create a new artist"})
                notifications = [] + pending_notifications
                pending_notifications.clear()
                return render_template('forms/create_artist.html', form=form, notifications=notifications)
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('forms/create_artist.html', form=form, notifications=notifications)
