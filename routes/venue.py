import json
from flask import render_template, url_for, redirect, request
from models.Venue import Venue
from models.Show import Show
from models.shared import db, pending_notifications
from forms.Venue import VenueForm


class VenueRouter:
    def view_all():
        notifications = [] + pending_notifications
        pending_notifications.clear()
        if request.method == 'POST':
            searchQuery = request.form.get('searchQuery')
            searchQuery = searchQuery.lstrip()
            if searchQuery:
                return render_template('venues.html', data={
                    'venues': Venue.query.filter(Venue.name.like('%' + searchQuery + '%')).all(),
                    'searchQuery': searchQuery
                }, notifications=notifications)
            else:
                return render_template('venues.html', data={
                    'venues': Venue.query.all(),
                    'searchQuery': ''
                }, notifications=notifications)
        else:
            return render_template('venues.html', data={
                'venues': Venue.query.all(),
                'searchQuery': ''
            }, notifications=notifications)

    def view_detail(venue_id):
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('venue.html', data={
            'venue': Venue.query.get(venue_id),
            'shows': Show.query.filter(Show.venue_id == venue_id)
        }, notifications=notifications)

    def create():
        form = VenueForm(request.form)
        if form.validate_on_submit():
            name = form.name.data
            city = form.city.data
            state = form.state.data
            address = form.address.data
            phone = form.phone.data
            genres = ','.join(form.genres.data)
            facebook_link = form.facebook_link.data
            venue = Venue(name=name, city=city, state=state, phone=phone, address=address, genres=genres, facebook_link=facebook_link)
            db.session.add(venue)
            try:
                db.session.commit()
                pending_notifications.append({"title": "Success", "body": "Created a new venue successfully"})
                return redirect(url_for('view_all_venues'))
            except Exception as err:
                db.session.rollback()
                pending_notifications.append({"title": "Failure", "body": "Invalid Data, Couldn't create a new venue"})
                notifications = [] + pending_notifications
                pending_notifications.clear()
                print(err)
                return render_template('forms/create_venue.html', form=form, notifications=notifications)
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('forms/create_venue.html', form=form, notifications=notifications)
