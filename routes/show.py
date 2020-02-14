from datetime import datetime
import json
from flask import render_template, url_for, redirect, request
from models.Show import Show
from models.shared import db, pending_notifications
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
        form = ShowForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            artist_id = form.artist_id.data
            venue_id = form.venue_id.data
            start_time = form.start_time.data
            show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time)
            db.session.add(show)
            try:
                db.session.commit()
                pending_notifications.append("Created a new show successfully")
                return redirect(url_for('view_all_shows'))
            except Exception:
                db.session.rollback()
                pending_notifications.append("Invalid Data, Couldn't create a new show")
                return redirect(url_for('create_show'))

        return render_template('forms/create_show.html', form=form, notifications=pending_notifications)
        