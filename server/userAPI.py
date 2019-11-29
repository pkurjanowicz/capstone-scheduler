from flask import Flask, Blueprint, jsonify, request, redirect
from db_instance import db
from models import User, Event
from datetime import datetime
import os
import flask
from sqlalchemy.exc import IntegrityError

user_api = Blueprint('user_api', __name__)


login_info = []
new_name_valid = []
password_match = []
registerBool = ''

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
    user_events = [{"id":event.id, "event_name": event.event_name, "details": event.details, "start_time": event.start_time.strftime("%Y-%m-%d %H:%M:%S"), "end_time":event.end_time.strftime("%Y-%m-%d %H:%M:%S"), "owner_id":event.owner_id} for event in event_instances]
    return jsonify({"all_events": user_events})

@user_api.route('/usersignup', methods=['POST'])
def add_user():
        new_user = User()
        new_user.username = request.json["new_user"]
        new_user.password = request.json["new_password"]
        new_confirm = request.json["new_pass_confirm"]
        db.session.add(new_user)

        

        if new_user.password != new_confirm:
            print("passwords do not match")
            
        else:

            password_match.append('True')
            try:
                db.session.commit()
                print("username added successfully")
                new_name_valid.append('True')
                print("newnamevalid line 50     " + str(new_name_valid))
                
                
                
            except IntegrityError as error:
                print("username already taken")

        if 'True' in new_name_valid and 'True' in password_match:
                registerBool = True
                print("registerBool is true")
        else:
                registerBool = False
        
        new_name_valid.clear()
        password_match.clear()
                
                
        print("registerBool line 68     " + str(registerBool))
        return jsonify({"newNameBool": registerBool})

@user_api.route('/newevent', methods=['POST'])
def add_event():
    new_event = Event()

    startTimeObject = datetime.strptime(request.json["event_start_time"], "%Y-%m-%d %H:%M:%S")
    endTimeObject = datetime.strptime(request.json["event_end_time"], "%Y-%m-%d %H:%M:%S")
    new_event.start_time = startTimeObject
    new_event.end_time = endTimeObject
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

@user_api.route('/user_login', methods=['POST'])
def user_login():
    
    entered_username = request.json["username_item"]
    entered_password = request.json["password_item"]
    login_info.append(entered_username)
    login_info.append(entered_password)
    
    return jsonify(success=True)

@user_api.route('/verify_login', methods=['GET'])
def verify_login():

    test_query = db.session.query(User).filter(User.username==login_info[0], 
    User.password==login_info[1]).scalar()
    
    if test_query != None:
        loginValid = True
        login_info.clear()
    else:
        loginValid = False
        login_info.clear()



    return jsonify({"loginbool": loginValid})
