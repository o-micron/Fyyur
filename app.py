import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.shared import db
from routes.artist import ArtistRoutes
from routes.show import ShowRoutes
from routes.venue import VenueRoutes


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

migrate = ''
with app.app_context():
    migrate = Migrate(app, db)


@app.route('/')
def intex():
    return render_template('index.html')


@app.route('/artists')
def artists():
    return ArtistRoutes.all()


@app.route('/artists/<artist_id>')
def artist(artist_id):
    return ArtistRoutes.detail(artist_id)

@app.route('/shows')
def shows():
    return ShowRoutes.all()


@app.route('/shows/<show_id>')
def show(show_id):
    return ShowRoutes.detail(show_id)

@app.route('/venues')
def venues():
    return VenueRoutes.all()


@app.route('/venues/<venue_id>')
def venue(venue_id):
    return VenueRoutes.detail(venue_id)