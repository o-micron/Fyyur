import json
import babel
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
def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(value, format)


app.jinja_env.filters['datetime'] = format_datetime
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
def intex():
    return render_template('index.html')


@app.route('/artists')
def view_all_artists():
    return ArtistRouter.view_all()


@app.route('/artists/<artist_id>')
def view_artist(artist_id):
    return ArtistRouter.view_detail(artist_id)

@app.route('/artists/create', methods=['POST'])
def create_artist():
    return ArtistRouter.create()


@app.route('/shows')
def view_all_shows():
    return ShowRouter.view_all()


@app.route('/shows/<show_id>')
def view_show(show_id):
    return ShowRouter.view_detail(show_id)

@app.route('/shows/create', methods=['POST'])
def create_show():
    return ShowRouter.create()

@app.route('/venues')
def view_all_venues():
    return VenueRouter.view_all()


@app.route('/venues/<venue_id>')
def view_venue(venue_id):
    return VenueRouter.view_detail(venue_id)

@app.route('/venues/create', methods=['POST'])
def create_venue():
    return VenueRouter.create()
## -----------------------------------------------------------------------------------------------