from flask import Blueprint, jsonify, request
from db_instance import db
from models import User, Event
import pytz

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods=['GET'])
def serve_all_users():
    user_instances = db.session.query(User).all()
    user_usernames = [{"id": user.id, "username": user.username} for user in user_instances]
    return jsonify({"usernames": user_usernames})

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
    # local_tz = pytz.timezone(new_event.timezone)
    python_start_time = new_event.start_time
    print(python_start_time)
    
    # new_event.event_name = request.json["event_name"]
    # python_start_time = request.json["start_time"]
    # new_event.end_time = request.json["end_time"]
    # new_event.details = request.json["event_details"]
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