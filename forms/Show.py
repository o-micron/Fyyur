from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL

class ShowForm(FlaskForm):
    artist_id = StringField('artist_id', validators=[DataRequired(message="Please enter a valid artist id")])
    venue_id = StringField('venue_id', validators=[DataRequired()], description="Please enter a valid venue id")
    start_time = DateTimeField('start_time', validators=[DataRequired(message="Please enter a valid start time")])