from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL

class ShowForm(Form):
    artist_id = StringField('artist_id', validators=[DataRequired()])
    venue_id = StringField('venue_id', validators=[DataRequired()])
    start_time = DateTimeField('start_time', validators=[DataRequired()])