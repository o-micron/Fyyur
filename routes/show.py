from flask import render_template
from models.Show import Show


class ShowRoutes:
    def all():
        return render_template('shows.html', data={
            'shows': Show.query.all()
        })

    def detail(show_id):
        return render_template('show.html', data={
            'show': Show.query.get(show_id)
        })
