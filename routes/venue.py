import json
from flask import render_template, url_for, redirect, request
from models.Venue import Venue
from models.Show import Show
from models.shared import db
from forms.Venue import VenueForm


class VenueRouter:
    def view_all():
        if request.method == 'POST':
            searchQuery = request.form.get('searchQuery')
            searchQuery = searchQuery.lstrip()
            if searchQuery:
                return render_template('venues.html', data={
                    'venues': Venue.query.filter(Venue.name.like('%' + searchQuery + '%')).all(),
                    'searchQuery': searchQuery
                })
            else:
                return render_template('venues.html', data={
                    'venues': Venue.query.all(),
                    'searchQuery': ''
                })
        else:
            return render_template('venues.html', data={
                'venues': Venue.query.all(),
                'searchQuery': ''
            })

    def view_detail(venue_id):
        return render_template('venue.html', data={
            'venue': Venue.query.get(venue_id),
            'shows': Show.query.filter(Show.venue_id == venue_id)
        })

    def create():
        if request.method == 'POST':
            data = json.loads(request.data)
            name = data['name']
            city = data['city']
            state = data['state']
            phone = data['phone']
            genres = ','.join(data['genres'])
            facebook_link = data['facebook_link']
            venue = Venue(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
            db.session.add(venue)
            db.session.commit()
            return redirect(url_for('view_all_venues'))
        elif request.method == 'GET':
            form = VenueForm()
            return render_template('forms/create_venue.html', form=form)
