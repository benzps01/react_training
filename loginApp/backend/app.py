from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from models import db, User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

load_dotenv()


app = Flask(__name__)
app.config.from_object(ApplicationConfig)

bcrypt = Bcrypt(app)
db.init_app(app)
with app.app_context():
    db.create_all()
    
CORS(app)

jwt = JWTManager(app)

@app.route('/register', methods=["POST"])
def register_user():
    email = request.get_json().get('email')
    password = request.get_json().get('password')
    
    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        abort(409)

    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
    new_user = User(email=email, password=hashed_password)
    new_user.insert()
        
    return jsonify({
        "id": new_user.id,
        "email": new_user.email,
        "password": new_user.password
    })
    
@app.route('/login', methods=['POST'])
def login_user():
    email = request.get_json().get('email')
    password = request.get_json().get('password')
    
    user = User.query.filter_by(email=email).first()

    if user is None:
        abort(401)
        
    if not bcrypt.check_password_hash(user.password, password):
        abort(401)
    expiration_time = timedelta(minutes=300)
    access_token = create_access_token(identity=email, expires_delta=expiration_time)
    return jsonify({
        'access_token': access_token,
        'id': user.id,
        'email': user.email,
        'password': user.password
    })
      
 
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': "User is not Authorized" 
    }), 401
    
@app.errorhandler(409)
def user_conflict(error):
    return jsonify({
        'success': False,
        'error': 409,
        'message': "User already exists" 
    }), 409

if __name__ == "__main__":
    app.run(debug=True)