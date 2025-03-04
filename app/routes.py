from flask import Blueprint, jsonify, request
from app.models import User
from app.auth import token_required
from bson import json_util
from app import bcrypt
from flask_jwt_extended import create_access_token
import json

main = Blueprint('main', __name__)


@main.route('/login', methods=['POST'])
def login():
    """
    Login
    ---
    params:
        email: str
        password: str
    responses:
      200: description: Returns a token
      401: description: Invalid credentials
    """
    email = request.args.get('email')
    password = request.args.get('password')

    if not email or not password:
        return jsonify({"message": "Could not verify, please provide email and password"}), 401

    user = User.find_by_email(email)
    if not user:
        return jsonify({"message": "User not found for the provided email"}), 401

    if bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401



@main.route('/users', methods=['GET'])
@token_required
def get_users():
    """
    Get all users
    ---
    responses:
      200: description: A list of users
    """
    users = User.find_all()
    return jsonify(json.loads(json_util.dumps(users))), 200

@main.route('/users/<id>', methods=['GET'])
@token_required
def get_user(id):
    """
    Get a user by ID
    ---
    responses:
      200: description: User details
      404: description: User not found
    """
    user = User.find_by_id(id)
    if user:
        return jsonify(json.loads(json_util.dumps(user))), 200
    return jsonify({"message": "User not found"}), 404

@main.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    data:
        name: str
        email: str
        password: str
    responses:
      201: description: User created
      400: description: Invalid input
    """
    data = request.json
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"message": "Missing required fields, please provide all the required fields"}), 400
    user_id = User.create(data['name'], data['email'], data['password'])
    return jsonify({"message": "User created", "id": user_id}), 201

@main.route('/users/<id>', methods=['PUT'])
@token_required
def update_user(id):
    """
    Update a user
    ---
    data:
        name: str
        email: str
        password: str
    responses:
      200: description: User updated
      404: description: User not found
    """
    user = User.find_by_id(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.json
    User.update(id, data)
    return jsonify({"message": "User updated"}), 200

@main.route('/users/<id>', methods=['DELETE'])
@token_required
def delete_user(id):
    """
    Delete a user
    ---
    responses:
      200: description: User deleted
      404: description: User not found
    """
    user = User.find_by_id(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    User.delete(id)
    return jsonify({"message": "User deleted"}), 200
