import os
import getpass


SECRET_KEY = os.urandom(32)
# Directory where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))
# debug mode
DEBUG = True
# Connect to database
# default config
db_config = {
    'dialect': 'postgresql',
    'username': getpass.getuser(),
    'password': '',
    'ip': 'localhost',
    'port': 5432,
    'name': 'toy'
}
# Check if there is a config file
# if it exists override the db_config above
try:
    with open('config.json') as f:
        db_config = json.load(f)
except:
    print("Using the default db configuration")

# Set the db url
DB_URL = '{dialect}://{username}:{password}@{ip}:{port}/{dbname}'.format(
    dialect=db_config['dialect'],
    username=db_config['username'],
    password=db_config['password'],
    ip=db_config['ip'],
    port=db_config['port'],
    dbname=db_config['name'])

SQLALCHEMY_DATABASE_URI = DB_URL
