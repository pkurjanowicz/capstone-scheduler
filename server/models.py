from db_instance import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    password = db.Column(db.String(500))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(500))
    start_time = db.Column(db.String(500))
    end_time = db.Column(db.String(500))
    details = db.Column(db.String(2000))
    ownder_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    shared_ids = db.Column(db.Integer, db.ForeignKey("user.id"))