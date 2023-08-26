import json
from functools import wraps
from flask import request

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwds):
        with open("gen/config.json") as configfile:
            trusted_keys = json.loads(configfile.read())['api_keys']

        user_auth = request.headers.get("Authorization")
        user_key = user_auth.split()[1]
        
        if user_key in trusted_keys:
            return f(*args, **kwds)
        else:
            raise AuthError({"code": "invalid_header", "description": "Unable to find appropriate key"}, 401)
        
    return decorated
