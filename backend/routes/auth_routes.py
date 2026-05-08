from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from models import db
from models.user import User

from utils.validators import validate_email, validate_password
from utils.token_helper import generate_reset_token, verify_reset_token
from extensions import bcrypt

auth_bp = Blueprint("auth", __name__)


# =========================
# SIGNUP
# =========================

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([full_name, email, password, confirm_password]):
        return jsonify({'error': 'All fields are required'}), 400

    if not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    if not validate_password(password):
        return jsonify({'error': 'Password must be at least 8 characters'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Account already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(full_name=full_name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Account created successfully'}), 201


# =========================
# LOGIN
# =========================

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}

    email = data.get('email')
    password = data.get('password')
    remember_me = data.get('remember_me', False)

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    if remember_me:
        access_token = create_access_token(identity=str(user.id), expires_delta=False)
    else:
        access_token = create_access_token(identity=str(user.id))

    return jsonify({
        'message': 'Login successful',
        'token': access_token,
        'user': {
            'id': user.id,
            'full_name': user.full_name,
            'email': user.email
        }
    }), 200


# =========================
# FORGOT PASSWORD
# =========================

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json() or {}
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if user:
        reset_token = generate_reset_token(email)
        reset_link = f"http://localhost:3000/reset-password/{reset_token}"
        print("RESET LINK:", reset_link)

    return jsonify({'message': 'If the email exists, a reset link has been generated.'}), 200


# =========================
# RESET PASSWORD
# =========================

@auth_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    email = verify_reset_token(token)
    if not email:
        return jsonify({'error': 'Reset link expired or invalid'}), 400

    data = request.get_json() or {}
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    if not validate_password(password):
        return jsonify({'error': 'Password must be at least 8 characters'}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user.password = hashed_password
    db.session.commit()

    return jsonify({'message': 'Password reset successful'}), 200
