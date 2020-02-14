from datetime import datetime
import json
from flask import render_template, url_for, redirect, request
from models.Show import Show
from models.shared import db
from forms.Show import ShowForm

class ShowRouter:
    def view_all():
        return render_template('shows.html', data={
            'shows': Show.query.all()
        })

    def view_detail(show_id):
        return render_template('show.html', data={
            'show': Show.query.get(show_id)
        })

    def create():
        if request.method == 'POST':
            data = json.loads(request.data)
            artist_id = data['artist_id']
            venue_id = data['venue_id']
            start_time = datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M:%S")
            show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time)
            db.session.add(show)
            db.session.commit()
            return redirect(url_for('view_all_shows'))
        elif request.method == 'GET':
            form = ShowForm()
            return render_template('forms/create_show.html', form=form)