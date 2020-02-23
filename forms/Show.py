from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, ValidationError
from wtforms.validators import DataRequired, AnyOf, URL, Regexp

class ShowForm(FlaskForm):
    artist_id = StringField('artist_id', validators=[Regexp('^[a-zA-Z0-9 ]+$', message="Please enter a valid artist name"), DataRequired()])
    venue_id = StringField('venue_id', validators=[Regexp('^[a-zA-Z0-9 ]+$', message="Please enter a valid venue name"), DataRequired()])
    start_time = DateTimeField('start_time', validators=[DataRequired(message="Please enter a valid data YYYY:MM:DD HH:MM:SS")])