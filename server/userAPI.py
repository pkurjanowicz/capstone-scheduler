from flask import Blueprint, jsonify, request
from db_instance import db
from models import User, Event

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