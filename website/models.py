from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True,  nullable=False)
    password = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    weight = db.Column(db.String(2),  nullable=False)
    phone = db.Column(db.String(11),  nullable=False)
    userRole = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(10),  nullable=False)
    bloodgroup = db.Column(db.String(3),  nullable=False)
    lastdonationdate = db.Column(db.String(15),  nullable=False)


class Fighter(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True,  nullable=False)
    password = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    weight = db.Column(db.String(2),  nullable=False)
    phone = db.Column(db.String(11),  nullable=False)
    userRole = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(10),  nullable=False)
    bloodgroup = db.Column(db.String(3),  nullable=False)
    hospital = db.Column(db.String(15),  nullable=False)

class Hero(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True,  nullable=False)
    password = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    weight = db.Column(db.String(2),  nullable=False)
    phone = db.Column(db.String(11),  nullable=False)
    userRole = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(10),  nullable=False)
    bloodgroup = db.Column(db.String(3),  nullable=False)
    ratings = db.Column(db.String(5), nullable=False, default="4")

from datetime import datetime


class BloodRequestDonate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requester_email = db.Column(db.String(40), nullable=False)
    requester_name = db.Column(db.String(20), nullable=False)
    donor_email = db.Column(db.String(40), nullable=True)
    donor_name = db.Column(db.String(40), nullable=True)
    blood_group = db.Column(db.String(5), nullable=False)   
    city = db.Column(db.String(20), nullable=False)
    hospital = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(20), default="pending")    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Emergency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requester_email = db.Column(db.String(40), nullable=False)
    requester_name = db.Column(db.String(20), nullable=False)
    requester_phome = db.Column(db.String(11),  nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)   
    city = db.Column(db.String(20), nullable=False)
    hospital = db.Column(db.String(40), nullable=False)   
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ratings_increased = db.Column(db.Float, nullable=False, default=0.0)
    donor_email = db.Column(db.String(120), nullable=False)
    requester_email = db.Column(db.String(120), nullable=False)
    request_created_at = db.Column(db.String(50), default=lambda: datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
