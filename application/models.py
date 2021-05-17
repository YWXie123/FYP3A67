from application import db
import datetime as dt
from sqlalchemy.orm import validates 
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    
class Entry(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    trestbps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.Integer)
    restecg = db.Column(db.Integer)
    thalach = db.Column(db.Integer)
    exang = db.Column(db.Integer)
    oldpeak = db.Column(db.Float)#float
    slope = db.Column(db.Integer)
    ca = db.Column(db.Integer)
    thal = db.Column(db.Integer)
    fk_userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    prediction = db.Column(db.Integer)
    predicted_on = db.Column(db.DateTime, nullable=False)

    @validates('age') 
    def validate_age(self, key, age):
        if age <0:
            raise AssertionError('Value must be positive')
        return age

    @validates('sex') 
    def validate_sex(self, key, sex):
        if sex != 0 and sex != 1:
            raise AssertionError('Value must be 0 or 1')
        return sex
    
    @validates('cp') 
    def validate_cp(self, key, cp):
        if cp < 0:
            raise AssertionError('Value must be 0 to 3')
        return cp

    @validates('trestbps') 
    def validate_trestbps(self, key, trestbps):
        if trestbps < 0:
            raise AssertionError('Value must be positive')
        return trestbps

    @validates('chol') 
    def validate_chol(self, key, chol):
        if chol < 0:
            raise AssertionError('Value must be positive')
        return chol

    @validates('fbs') 
    def validate_fbs(self, key, fbs):
        if fbs != 0 and fbs != 1:
            raise AssertionError('Value must be 0 or 1')
        return fbs

    @validates('restecg') 
    def validate_restecg(self, key, restecg):
        if restecg < 0:
            raise AssertionError('Value must be positive')
        return restecg

    @validates('thalach') 
    def validate_thalach(self, key, thalach):
        if thalach < 0:
            raise AssertionError('Value must be positive')
        return thalach

    @validates('exang') 
    def validate_exang(self, key, exang):
        if exang != 0 and exang != 1:
            raise AssertionError('Value must be 0 or 1')
        return exang

    @validates('oldpeak') 
    def validate_oldpeak(self, key, oldpeak):
        if oldpeak < 0:
            raise AssertionError('Value must be positive')
        return oldpeak

    @validates('slope') 
    def validate_slope(self, key, slope):
        if slope < 0:
            raise AssertionError('Value must be positive')
        return slope

    @validates('ca') 
    def validate_ca(self, key, ca):
        if ca < 0:
            raise AssertionError('Value must be positive')
        return ca

    @validates('thal') 
    def validate_thal(self, key, thal):
        if thal < 0:
            raise AssertionError('Value must be positive')
        return thal
    
    @validates('prediction') 
    def validate_thal(self, key, prediction):
        if prediction != 0 and prediction != 1:
            raise AssertionError('Value must be 0 or 1')
        return prediction
