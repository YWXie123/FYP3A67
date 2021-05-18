from application import db
import datetime as dt
from sqlalchemy.orm import backref, validates
 
class Staff(db.Model):
    __tablename__ = 'staff'
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staffid = db.relationship('Staff Id',backref = 'staff', lazy=True)
    name = db.Column(db.String(20))
    position = db.Column(db.String(80))
    department = db.Column(db.String(20))

class SearchHist(db.Model):
    __tablename__ = 'search_history'
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staffid = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable = False)
    asked_on = db.Column(db.DateTime, nullable = False)
    question = db.Column(db.String(200))

class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(300))

class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(300))