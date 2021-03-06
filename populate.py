import psycopg2
import json

connection = psycopg2.connect('dbname=toy user=omar')

cursor = connection.cursor()

artists = [
    {
        "id": 4,
        "name": "Guns N Petals",
        "genres": ["Rock n Roll"],
        "city": "San Francisco",
        "state": "CA",
        "phone": "326-123-5000",
        "website": "https://www.gunsnpetalsband.com",
        "facebook_link": "https://www.facebook.com/GunsNPetals",
        "seeking_venue": True,
        "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
        "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
        "past_shows": [{
            "venue_id": 1,
            "venue_name": "The Musical Hop",
            "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
            "start_time": "2019-05-21T21:30:00.000Z"
        }],
        "upcoming_shows": [],
        "past_shows_count": 1,
        "upcoming_shows_count": 0,
    },
    {
        "id": 5,
        "name": "Matt Quevedo",
        "genres": ["Jazz"],
        "city": "New York",
        "state": "NY",
        "phone": "300-400-5000",
        "facebook_link": "https://www.facebook.com/mattquevedo923251523",
        "seeking_venue": False,
        "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        "past_shows": [{
            "venue_id": 3,
            "venue_name": "Park Square Live Music & Coffee",
            "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
            "start_time": "2019-06-15T23:00:00.000Z"
        }],
        "upcoming_shows": [],
        "past_shows_count": 1,
        "upcoming_shows_count": 0,
    },
    {
        "id": 6,
        "name": "The Wild Sax Band",
        "genres": ["Jazz", "Classical"],
        "city": "San Francisco",
        "state": "CA",
        "phone": "432-325-5432",
        "seeking_venue": False,
        "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
        "past_shows": [],
        "upcoming_shows": [{
            "venue_id": 3,
            "venue_name": "Park Square Live Music & Coffee",
            "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
            "start_time": "2035-04-01T20:00:00.000Z"
        }, {
            "venue_id": 3,
            "venue_name": "Park Square Live Music & Coffee",
            "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
            "start_time": "2035-04-08T20:00:00.000Z"
        }, {
            "venue_id": 3,
            "venue_name": "Park Square Live Music & Coffee",
            "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
            "start_time": "2035-04-15T20:00:00.000Z"
        }],
        "past_shows_count": 0,
        "upcoming_shows_count": 3,
    }
]

venues = [
    {
        "id": 1,
        "name": "The Musical Hop",
        "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
        "address": "1015 Folsom Street",
        "city": "San Francisco",
        "state": "CA",
        "phone": "123-123-1234",
        "website": "https://www.themusicalhop.com",
        "facebook_link": "https://www.facebook.com/TheMusicalHop",
        "seeking_talent": True,
        "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
        "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
        "past_shows": [{
            "artist_id": 4,
            "artist_name": "Guns N Petals",
            "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
            "start_time": "2019-05-21T21:30:00.000Z"
        }],
        "upcoming_shows": [],
        "past_shows_count": 1,
        "upcoming_shows_count": 0,
    },
    {
        "id": 2,
        "name": "The Dueling Pianos Bar",
        "genres": ["Classical", "R&B", "Hip-Hop"],
        "address": "335 Delancey Street",
        "city": "New York",
        "state": "NY",
        "phone": "914-003-1132",
        "website": "https://www.theduelingpianos.com",
        "facebook_link": "https://www.facebook.com/theduelingpianos",
        "seeking_talent": False,
        "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
        "past_shows": [],
        "upcoming_shows": [],
        "past_shows_count": 0,
        "upcoming_shows_count": 0,
    },
    {
        "id": 3,
        "name": "Park Square Live Music & Coffee",
        "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
        "address": "34 Whiskey Moore Ave",
        "city": "San Francisco",
        "state": "CA",
        "phone": "415-000-1234",
        "website": "https://www.parksquarelivemusicandcoffee.com",
        "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
        "seeking_talent": False,
        "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
        "past_shows": [{
            "artist_id": 5,
            "artist_name": "Matt Quevedo",
            "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
            "start_time": "2019-06-15T23:00:00.000Z"
        }],
        "upcoming_shows": [{
            "artist_id": 6,
            "artist_name": "The Wild Sax Band",
            "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
            "start_time": "2035-04-01T20:00:00.000Z"
        }, {
            "artist_id": 6,
            "artist_name": "The Wild Sax Band",
            "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
            "start_time": "2035-04-08T20:00:00.000Z"
        }, {
            "artist_id": 6,
            "artist_name": "The Wild Sax Band",
            "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
            "start_time": "2035-04-15T20:00:00.000Z"
        }],
        "past_shows_count": 1,
        "upcoming_shows_count": 1,
    }
]

shows = [
    {
        "venue_id": 1,
        "venue_name": "The Musical Hop",
        "artist_id": 4,
        "artist_name": "Guns N Petals",
        "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
        "start_time": "2019-05-21T21:30:00.000Z"
    }, {
        "venue_id": 3,
        "venue_name": "Park Square Live Music & Coffee",
        "artist_id": 5,
        "artist_name": "Matt Quevedo",
        "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        "start_time": "2019-06-15T23:00:00.000Z"
    }, {
        "venue_id": 3,
        "venue_name": "Park Square Live Music & Coffee",
        "artist_id": 6,
        "artist_name": "The Wild Sax Band",
        "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
        "start_time": "2035-04-01T20:00:00.000Z"
    }, {
        "venue_id": 3,
        "venue_name": "Park Square Live Music & Coffee",
        "artist_id": 6,
        "artist_name": "The Wild Sax Band",
        "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
        "start_time": "2035-04-08T20:00:00.000Z"
    }, {
        "venue_id": 3,
        "venue_name": "Park Square Live Music & Coffee",
        "artist_id": 6,
        "artist_name": "The Wild Sax Band",
        "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
        "start_time": "2035-04-15T20:00:00.000Z"
    }
]

for artist in artists:
    name = artist.get('name') if 'name' in artist else ""
    genres = ','.join(artist.get('genres')) if 'genres' in artist else ""
    city = artist.get('city') if 'city' in artist else ""
    state = artist.get('state') if 'state' in artist else ""
    phone = artist.get('phone') if 'phone' in artist else ""
    website = artist.get('website') if 'website' in artist else ""
    seeking_venue_description = artist.get('seeking_venue_description') if 'seeking_venue_description' in artist else ""
    image_link = artist.get('image_link') if 'image_link' in artist else ""
    facebook_link = artist.get('facebook_link') if 'facebook_link' in artist else ""
    cmd = """
    INSERT INTO artists
    (name, genres, city, state, phone, website, seeking_venue_description, image_link, facebook_link)
    VALUES
    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
    """ % (name, genres, city, state, phone, website, seeking_venue_description, image_link, facebook_link)
    try:
        cursor.execute(cmd)
    except psycopg2.IntegrityError:
        connection.rollback()
    else:
        connection.commit()

for venue in venues:
    name = venue.get('name') if 'name' in venue else ""
    genres = ','.join(venue.get('genres')) if 'genres' in venue else ""
    city = venue.get('city') if 'city' in venue else ""
    state = venue.get('state') if 'state' in venue else ""
    address = venue.get('address') if 'address' in venue else ""
    phone = venue.get('phone') if 'phone' in venue else ""
    seeking_talent_description = venue.get('seeking_talent_description') if 'seeking_talent_description' in venue else ""
    website = venue.get('website') if 'website' in venue else ""
    image_link = venue.get('image_link') if 'image_link' in venue else ""
    facebook_link = venue.get('facebook_link') if 'facebook_link' in venue else ""
    cmd = """
    INSERT INTO venues
    (name, genres, city, state, address, phone, seeking_talent_description, website, image_link, facebook_link)
    VALUES
    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
    """ % (name, genres, city, state, address, phone, seeking_talent_description, website, image_link, facebook_link)
    try:
        cursor.execute(cmd)
    except psycopg2.IntegrityError:
        connection.rollback()
    else:
        connection.commit()
        
for show in shows:
    cmd = """
    INSERT INTO shows
    (start_time, artist_id, venue_id)
    VALUES
    ('%s',(SELECT id FROM artists WHERE name='%s'), (SELECT id from venues WHERE name='%s'));
    """ % (show.get('start_time'), show.get('artist_name'), show.get('venue_name'))
    try:
        cursor.execute(cmd)
    except psycopg2.IntegrityError:
        connection.rollback()
    else:
        connection.commit()

# -------------------------------------------------------------------------------------------------
# ADD EXTRA MOCK DATA
# -------------------------------------------------------------------------------------------------
with open('data/artists.json', 'r') as file:
    mock_artists = json.load(file)
    for artist in mock_artists:
        name = artist.get('name') if 'name' in artist else ""
        genres = ','.join(artist.get('genres')) if 'genres' in artist else ""
        city = artist.get('city') if 'city' in artist else ""
        state = artist.get('state') if 'state' in artist else ""
        phone = artist.get('phone') if 'phone' in artist else ""
        website = artist.get('website') if 'website' in artist else ""
        seeking_venue_description = artist.get('seeking_venue_description') if 'seeking_venue_description' in artist else ""
        image_link = artist.get('image_link') if 'image_link' in artist else ""
        facebook_link = artist.get('facebook_link') if 'facebook_link' in artist else ""
        cmd = """
        INSERT INTO artists
        (name, genres, city, state, phone, website, seeking_venue_description, image_link, facebook_link)
        VALUES
        ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
        """ % (name, genres, city, state, phone, website, seeking_venue_description, image_link, facebook_link)
        try:
            cursor.execute(cmd)
        except psycopg2.IntegrityError:
            connection.rollback()
        else:
            connection.commit()

with open('data/venues.json', 'r') as file:
    mock_venues = json.load(file)
    for venue in mock_venues:
        name = venue.get('name') if 'name' in venue else ""
        genres = ','.join(venue.get('genres')) if 'genres' in venue else ""
        city = venue.get('city') if 'city' in venue else ""
        state = venue.get('state') if 'state' in venue else ""
        address = venue.get('address') if 'address' in venue else ""
        phone = venue.get('phone') if 'phone' in venue else ""
        seeking_talent_description = venue.get('seeking_talent_description') if 'seeking_talent_description' in venue else ""
        website = venue.get('website') if 'website' in venue else ""
        image_link = venue.get('image_link') if 'image_link' in venue else ""
        facebook_link = venue.get('facebook_link') if 'facebook_link' in venue else ""
        cmd = """
        INSERT INTO venues
        (name, genres, city, state, address, phone, seeking_talent_description, website, image_link, facebook_link)
        VALUES
        ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
        """ % (name, genres, city, state, address, phone, seeking_talent_description, website, image_link, facebook_link)
        try:
            cursor.execute(cmd)
        except psycopg2.IntegrityError:
            connection.rollback()
        else:
            connection.commit()
# -------------------------------------------------------------------------------------------------

cursor.close()
connection.close()
