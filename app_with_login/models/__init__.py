from werkzeug.security import generate_password_hash, check_password_hash
from app_with_login.ext.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)