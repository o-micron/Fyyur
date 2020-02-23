import json
from flask import render_template, url_for, redirect, request, flash, jsonify
from models.Artist import Artist
from forms.Artist import ArtistForm
from models.Show import Show
from models.shared import db, fetch_unread_notifications

DEFAULT_PAGINATION_COUNT = 8

class ArtistRouter:
    def view_all():
        searchQuery = ''
        items = Artist.query.order_by('name').all()
        if request.method == 'POST':
            searchQuery = request.form.get('searchQuery').lstrip().rstrip()
            items = Artist.search_for(searchQuery)
        else:
            if 'filter' in request.args:
                if request.args['filter'] == 'recent':
                    items = Artist.fetch_recent(request.args.get('cpp', default=Artist.COUNT_PER_PAGE, type=int))
                elif request.args['filter'] == 'top':
                    items = Artist.fetch_top(request.args.get('cpp', default=Artist.COUNT_PER_PAGE, type=int))
        return render_template('artists.html', data={
            'artists': items,
            'searchQuery': searchQuery
        }, notifications=fetch_unread_notifications())

    def view_detail(artist_id):
        return render_template('artist.html', data={
            'artist': Artist.query.get(artist_id),
            'shows': Show.query.filter(Show.artist_id == artist_id).order_by('start_time').all()
        }, notifications=fetch_unread_notifications())

    def create():
        form = ArtistForm(request.form)
        if form.validate_on_submit():
            artist = Artist.create_from_form(form)
            if artist.insert():
                return redirect(url_for('view_all_artists'))
            return render_template('forms/create_artist.html', form=form, notifications=fetch_unread_notifications())
        return render_template('forms/create_artist.html', form=form, notifications=fetch_unread_notifications())

    def autocomplete():
        return jsonify({ 'artists_names': [artist.name for artist in Artist.query.order_by('name').all()] })
