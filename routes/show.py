from datetime import datetime
import json
from flask import render_template, url_for, redirect, request
from models.Show import Show
from models.shared import db, fetch_unread_notifications
from forms.Show import ShowForm

class ShowRouter:
    def view_all():
        return render_template('shows.html', data={
            'shows': Show.query.order_by('start_time').all()
        }, notifications=fetch_unread_notifications())

    def view_detail(show_id):
        return render_template('show.html', data={
            'show': Show.query.get(show_id)
        }, notifications=fetch_unread_notifications())

    def create():
        form = ShowForm(request.form)
        if form.validate_on_submit():
            show = Show.create_from_form(form)
            if show.insert():
                return redirect(url_for('view_all_shows'))
            return render_template('forms/create_show.html', form=form, notifications=fetch_unread_notifications())
        return render_template('forms/create_show.html', form=form, notifications=fetch_unread_notifications())