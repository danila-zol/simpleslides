import json
from functools import wraps
from flask import request
from jsonschema import validate
from schemas import userinit_schema

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwds):
        user_auth = request.headers.get("Authorization")
        val = validator.key

        val(user_auth)

        return f(*args, **kwds)
        
    return decorated

class validator:
    def __init__(self):
        pass

    def key(auth):
        method = auth.split()[0]
        if (method.lower() != 'bearer'):
            raise AuthError({"code" : "invalid_method", "description" : "Only supported method: Bearer"})
        
        with open("gen/config.json") as configfile:
            trusted_keys = json.loads(configfile.read())['api_keys']
        key = auth.split()[1]
        if not key in trusted_keys:
            raise AuthError({"code" : "invalid_key", "description" : "Invalid API key"})
        
        return 1
        
    def user_init(info):
        validate(instance=info, schema=userinit_schema)
        