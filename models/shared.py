from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# this is a simple notification queue, volatile, I know, not persistant ..
# in ideal scenarios one would want to create that for each user in the db
# we don't have users now, so .... moving on :D
pending_notifications = []

def fetch_unread_notifications():
    notifications = [] + pending_notifications
    pending_notifications.clear()
    return notifications