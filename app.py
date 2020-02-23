import json
import babel
from datetime import datetime
import dateutil.parser
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.shared import db
from routes.artist import ArtistRouter
from routes.show import ShowRouter
from routes.venue import VenueRouter

## -----------------------------------------------------------------------------------------------
## Setup
## -----------------------------------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

migrate = ''
with app.app_context():
    migrate = Migrate(app, db)
## -----------------------------------------------------------------------------------------------


## -----------------------------------------------------------------------------------------------
## Filters
## -----------------------------------------------------------------------------------------------
app.jinja_env.filters['date_now'] = lambda _: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
app.jinja_env.filters['is_date_in_the_past'] = lambda d: d < datetime.now()
app.jinja_env.filters['is_date_in_the_future'] = lambda d: d > datetime.now()
## -----------------------------------------------------------------------------------------------


## -----------------------------------------------------------------------------------------------
## Controllers
## -----------------------------------------------------------------------------------------------
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html')


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists', methods=['GET', 'POST'])
def view_all_artists():
    return ArtistRouter.view_all()


@app.route('/artists/<artist_id>')
def view_artist(artist_id):
    return ArtistRouter.view_detail(artist_id)

@app.route('/artists/create', methods=['GET', 'POST'])
def create_artist():
    return ArtistRouter.create()

@app.route('/artists/autocomplete', methods=['GET'])
def autocomplete_artist():
    return ArtistRouter.autocomplete()


@app.route('/shows')
def view_all_shows():
    return ShowRouter.view_all()


@app.route('/shows/<show_id>')
def view_show(show_id):
    return ShowRouter.view_detail(show_id)

@app.route('/shows/create', methods=['GET', 'POST'])
def create_show():
    return ShowRouter.create()

@app.route('/venues', methods=['GET', 'POST'])
def view_all_venues():
    return VenueRouter.view_all()

@app.route('/venues/<venue_id>')
def view_venue(venue_id):
    return VenueRouter.view_detail(venue_id)

@app.route('/venues/create', methods=['GET', 'POST'])
def create_venue():
    return VenueRouter.create()

@app.route('/venues/autocomplete', methods=['GET'])
def autocomplete_venue():
    return VenueRouter.autocomplete()
## -----------------------------------------------------------------------------------------------