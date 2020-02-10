import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.shared import db
from routes.artist import ArtistRoutes
from routes.venue import VenueRoutes


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/')
def intex():
    return render_template('index.html')


@app.route('/artists')
def artists():
    return ArtistRoutes.all()


@app.route('/artists/<artist_id>')
def artist():
    return ArtistRoutes.detail()


@app.route('/venues')
def venues():
    return VenueRoutes.all()


@app.route('/venues/<venue_id>')
def venue():
    return VenueRoutes.detail()
