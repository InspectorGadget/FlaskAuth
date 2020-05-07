from app import app
from flask import request, jsonify
from app.models.user import User
from app.models.token import Token
from cerberus import Validator

@app.route('/auth', methods=['POST'])
def authenticate():
    if not request.json:
        return {'message': 'Request is not JSON.'}, 500
    
    schema = {
        'username': {'type': 'string', 'required': True},
        'url': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True}
    }

    validator = Validator(schema)
    if not validator.validate(request.json):
        return {'message': 'Required parameters are missing!'}, 500

    payload = request.get_json()
    username = payload['username'].lower()
    url = payload['url']
    password = payload['password']

    user = User.find_by_username_password(username=username, password=password)
    if user:
        try:
            Token.delete_all_tokens(user.id)
            token = Token(url=url, user_id=user.id)
            token.save()
            if token:
                return {'message': 'Token has been created', 'token': token.token}, 201
            else:
                return {'message': 'Unable to generate token.'}, 500
        except:
            return {'message': 'Unable to generate token.'}, 500
    else:
        return {'message': 'User does not exist!'}, 404