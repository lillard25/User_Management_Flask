from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity

def token_required(f):
    @wraps(f)
    @jwt_required()
    def decorated(*args, **kwargs):
        get_jwt_identity()
        return f(*args, **kwargs)
    return decorated
