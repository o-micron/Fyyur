from datetime import datetime
import json
from flask import render_template, url_for, redirect, request
from models.Show import Show
from models.shared import db, pending_notifications
from forms.Show import ShowForm

class ShowRouter:
    def view_all():
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('shows.html', data={
            'shows': Show.query.order_by('start_time').all()
        }, notifications=notifications)

    def view_detail(show_id):
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('show.html', data={
            'show': Show.query.get(show_id)
        }, notifications=notifications)

    def create():
        form = ShowForm(request.form)
        if form.validate_on_submit():
            artist_id = form.artist_id.data
            venue_id = form.venue_id.data
            start_time = form.start_time.data
            show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time)
            db.session.add(show)
            try:
                db.session.commit()
                pending_notifications.append({"title": "Success", "body": "Created a new show successfully"})
                return redirect(url_for('view_all_shows'))
            except Exception:
                db.session.rollback()
                pending_notifications.append({"title": "Failure", "body": "Invalid Data, Couldn't create a new show"})
                notifications = [] + pending_notifications
                pending_notifications.clear()
                return render_template('forms/create_show.html', form=form, notifications=notifications)
        notifications = [] + pending_notifications
        pending_notifications.clear()
        return render_template('forms/create_show.html', form=form, notifications=notifications)
        