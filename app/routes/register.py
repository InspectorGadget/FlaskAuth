from app import app
from flask import request, jsonify
from app.models.user import User
from cerberus import Validator

@app.route('/register', methods=['POST'])
def register():
    if not request.json:
        return {'message': 'Request is not JSON.'}, 500
    
    schema = {
        'username': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True}
    }

    validator = Validator(schema)
    if not validator.validate(request.json):
        return {'message': 'Required parameters are missing!'}, 500

    payload = request.get_json()
    username = payload['username'].lower()
    email = payload['email'].lower()
    password = payload['password']

    if User.find_by_username(username=username) or User.find_by_email(email=email):
        return {'message': 'A user exists!'}, 500

    try:
        user = User(email, username, password)
        user.save()
        return {'message': 'Successfully registered.'}, 201
    except:
        return {'message': 'Unable to register user.'}, 500