import json
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
    return babel.dates.format_datetime(date, format)


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
def artists():
    return ArtistRouter.all()


@app.route('/artists/<artist_id>')
def artist(artist_id):
    return ArtistRouter.detail(artist_id)


@app.route('/shows')
def shows():
    return ShowRouter.all()


@app.route('/shows/<show_id>')
def show(show_id):
    return ShowRouter.detail(show_id)


@app.route('/venues')
def venues():
    return VenueRouter.all()


@app.route('/venues/<venue_id>')
def venue(venue_id):
    return VenueRouter.detail(venue_id)
## -----------------------------------------------------------------------------------------------