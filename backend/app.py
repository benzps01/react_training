import os, sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, abort, jsonify
from flask_cors import CORS
from models import setup_db, Meetups, db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")
        
        return response
    
    @app.route('/meetups', methods=['GET','POST']) 
    def create_meetup():
        if request.method == 'POST':
            try:
                title = request.get_json()['title']
                image = request.get_json()['image']
                address = request.get_json()['address']
                description = request.get_json()['description']
                print("title", title)
                
                new_meetup = Meetups(title=title, image=image, address=address, description=description)
                new_meetup.insert()
                
                return jsonify({
                    'success': True,
                })
            except:
                db.session.rollback()
                print(sys.exc_info())
                abort(422)
        else:
            meetups = Meetups.query.all();
            all_meetups = [meetup.format() for meetup in meetups]
            return all_meetups             
    
    return app