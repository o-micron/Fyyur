import json
from flask import render_template, url_for, redirect, request, jsonify
from models.Venue import Venue
from models.Show import Show
from models.shared import db, fetch_unread_notifications
from forms.Venue import VenueForm


class VenueRouter:
    def view_all():
        searchQuery = ''
        items = Venue.group_by_location()
        if request.method == 'POST':
            searchQuery = request.form.get('searchQuery').lstrip().rstrip()
            items = Venue.search_for(searchQuery)
        else:
            if 'filter' in request.args:
                if request.args['filter'] == 'recent':
                    items = Venue.fetch_recent(request.args.get('cpp', default=Venue.COUNT_PER_PAGE, type=int))
                if request.args['filter'] == 'top':
                    items = Venue.fetch_top(request.args.get('cpp', default=Venue.COUNT_PER_PAGE, type=int))
        return render_template('venues.html', data={
            'venues': items,
            'searchQuery': searchQuery
        }, notifications=fetch_unread_notifications())

    def view_detail(venue_id):
        return render_template('venue.html', data={
            'venue': Venue.query.get(venue_id),
            'shows': Show.query.filter(Show.venue_id == venue_id).order_by('start_time').all()
        }, notifications=fetch_unread_notifications())

    def create():
        form = VenueForm(request.form)
        if form.validate_on_submit():
            venue = Venue.create_from_form(form)
            if venue.insert():
                return redirect(url_for('view_all_venues'))
            return render_template('forms/create_venue.html', form=form, notifications=fetch_unread_notifications())
        return render_template('forms/create_venue.html', form=form, notifications=fetch_unread_notifications())

    def autocomplete():
        return jsonify({ 'venues_names': [venue.name for venue in Venue.query.order_by('name').all()] })