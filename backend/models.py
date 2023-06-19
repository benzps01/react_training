from flask_sqlalchemy import SQLAlchemy
import json

database = "postgresql://_beast101_:admin@localhost:5432/meetupdb"

db = SQLAlchemy()

def setup_db(app, database_path=database):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app #type: ignore
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
class Meetups(db.Model):
    __tablename__ = "meetups"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)  
    
    def __init__(self, title, image, address, description):
        self.title = title
        self.image = image
        self.address = address
        self.description = description
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'image': self.image,
        'address': self.address,
        'description': self.description
        }
        