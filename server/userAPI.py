from flask import Blueprint, jsonify, request
from db_instance import db
from models import User, Event
from datetime import datetime
import pytz

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET'])
def serve_all_users():
    user_instances = db.session.query(User).all()
    user_usernames = [{"id": user.id, "username": user.username} for user in user_instances]
    return jsonify({"usernames": user_usernames})

@user_api.route('/getevents', methods=['GET'])
def serve_all_events():
    event_instances = db.session.query(Event).all()
    user_events = [{"event_name": event.event_name, "details": event.details, "owner_id":event.owner_id} for event in event_instances]
    return jsonify({"all_events": user_events})

@user_api.route('/usersignup', methods=['POST'])
def add_user():
    new_user = User()
    new_user.username = request.json["new_user"]
    db.session.add(new_user)
    db.session.commit()
    return jsonify(success=True)

@user_api.route('/newevent', methods=['POST'])
def add_event():
    new_event = Event()
    year = request.json["year"]
    month = request.json["month"]
    day = request.json["day"]
    hour = request.json["hour"]
    minute = request.json["minute"]
    second = request.json["second"]

    final_datetime = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

    # local_tz = pytz.timezone(new_event.timezone)
    # python_start_time = new_event.start_time
    # print(python_start_time)
    
    new_event.start_time = final_datetime
    new_event.event_name = request.json["event_name"]
    new_event.details = request.json["event_details"]
    new_event.owner_id = request.json["owner_id"]
    # new_event.end_time = request.json["end_time"]
    if new_event.event_name != "" and new_event.details != "":
        db.session.add(new_event)
        db.session.commit()
    return jsonify(success=True)

# @user_api.route('/user', methods=['PATCH'])
# def toggle_done():
#     user_id = request.json["id"]
#     target_user = db.session.query(User).filter_by(id=user_id).first()
#     # target_user.password = ""
#     db.session.add(target_user)
#     db.session.commit()
#     return jsonify(success=True)

# @user_api.route('/user/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     target_user = db.session.query(User).filter_by(id=user_id).first()
#     db.session.delete(target_user)
#     db.session.commit()
#     return jsonify(success=True)