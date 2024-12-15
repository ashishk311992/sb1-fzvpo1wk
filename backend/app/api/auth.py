from flask import jsonify, request
from app import db
from app.models.user import User
from app.api import bp
from app.utils.auth import create_token, admin_required
from app.utils.email import send_welcome_email

@bp.route('/auth/register', methods=['POST'])
@admin_required
def register_user():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    user = User(
        email=data['email'],
        name=data['name'],
        role=data.get('role', 'user'),
        company=data.get('company')
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    send_welcome_email(user.email, user.name, data['password'])
    
    return jsonify(user.to_dict()), 201

@bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):
        token = create_token(user.id)
        return jsonify({'token': token, 'user': user.to_dict()})
    
    return jsonify({'error': 'Invalid credentials'}), 401