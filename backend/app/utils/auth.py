from functools import wraps
from flask import jsonify, request, g
from jose import jwt
from datetime import datetime, timedelta
from app.models.user import User
from app import db

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['user_id']
    except:
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'No token provided'}), 401
        
        user_id = verify_token(token.split()[1])
        if not user_id:
            return jsonify({'error': 'Invalid token'}), 401
        
        g.current_user = User.query.get(user_id)
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'No token provided'}), 401
        
        user_id = verify_token(token.split()[1])
        if not user_id:
            return jsonify({'error': 'Invalid token'}), 401
        
        user = User.query.get(user_id)
        if user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        g.current_user = user
        return f(*args, **kwargs)
    return decorated_function