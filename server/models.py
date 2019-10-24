from db_instance import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500), unique=True)
    password = db.Column(db.String(500))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timezone = ""
    event_name = db.Column(db.String(500))
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.String(2000))
    ownder_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    shared_ids = db.Column(db.Integer, db.ForeignKey("user.id"))