from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(345), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    