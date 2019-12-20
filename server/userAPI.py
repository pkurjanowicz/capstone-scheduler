from flask import Blueprint, jsonify, request
from db_instance import db
from models import User, Event, Invites
from datetime import datetime

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET'])
def serve_all_users():
    user_instances = db.session.query(User).all()
    user_usernames = [{"id": user.id, "username": user.username} for user in user_instances]
    return jsonify({"usernames": user_usernames})

@user_api.route('/getevents', methods=['GET'])
def serve_all_events():
    event_instances = db.session.query(Event).all()
    # do not change the %Y-%m-%d %H:%M:%S format of these times in the line
    #  below because this is being used in that format on the calendar ** PK
    user_events = [{"id":event.id, "event_name": event.event_name, "details": event.details, "start_time": event.start_time.strftime("%Y-%m-%d %H:%M:%S"), "end_time":event.end_time.strftime("%Y-%m-%d %H:%M:%S"), "all_day": event.all_day, "owner_id":event.owner_id, "drag": event.drag} for event in event_instances]
    event = [event.id for event in event_instances]
    print(event)
    return jsonify({"all_events": user_events})

@user_api.route('/getinvites', methods=['POST'])
def get_invites():
    event_id = request.json["event_id"]
    event_invites = Invites.query.filter_by(event_id=event_id).all()
    event_invites_array = [{'email':event_invite.invitee_email, 'accepted': event_invite.accepted} for event_invite in event_invites]
    return jsonify({'all_invites': event_invites_array})

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

    startTimeObject = datetime.strptime(request.json["event_start_time"], "%Y-%m-%d %H:%M:%S")
    endTimeObject = datetime.strptime(request.json["event_end_time"], "%Y-%m-%d %H:%M:%S")
    new_event.start_time = startTimeObject
    new_event.end_time = endTimeObject
    new_event.all_day = request.json["all_day"]
    new_event.drag = request.json["drag"]
    new_event.event_name = request.json["event_name"]
    new_event.details = request.json["event_details"]
    new_event.owner_id = request.json["owner_id"]
    if new_event.owner_id != "" and new_event.event_name != "" and new_event.start_time != "":
        db.session.add(new_event)
        db.session.commit()
    return jsonify(success=True, event_id=new_event.id)

@user_api.route('/deleteevent', methods=['DELETE'])
def delete_event():
    event_id = request.json["event_id"]
    to_delete = Event.query.filter_by(id=event_id).one()
    db.session.delete(to_delete)
    db.session.commit()
    return jsonify(success=True)

@user_api.route('/updateevent', methods=['PATCH'])
def update_event():
    event_id = request.json["id"]
    start_time = datetime.strptime(request.json["start_time"], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(request.json["end_time"], "%Y-%m-%d %H:%M:%S")
    drag = request.json["drag"]
    target_event = db.session.query(Event).filter_by(id=event_id).first()
    target_event.start_time = start_time
    target_event.end_time = end_time
    target_event.drag = drag
    db.session.commit()
    return jsonify(success=True)