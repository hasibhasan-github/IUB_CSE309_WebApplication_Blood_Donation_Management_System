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