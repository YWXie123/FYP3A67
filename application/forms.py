from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, PasswordField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange

class PredictionForm(FlaskForm):
    age   = FloatField("Age", 
               validators=[InputRequired(), NumberRange(0,200)])
    sex   = FloatField("Sex",
               validators=[InputRequired(), NumberRange(0,1)])
    cp   = FloatField("Chest Pain Type(cp)",
               validators=[InputRequired(), NumberRange(0,3)])
    trestbps   = FloatField("Resting blood pressure(trestbps)",
               validators=[InputRequired(), NumberRange(0,300)])
    chol   = FloatField("Serum Cholestoral(chol)",
               validators=[InputRequired(), NumberRange(0,1000)])
    fbs   = FloatField("Fasting Blood Sugar > 120 mg/dl(fbs)",
               validators=[InputRequired(), NumberRange(0,1)])
    restecg   = FloatField("Resting Electrocardiographic Results(restecg)",
               validators=[InputRequired(), NumberRange(0,2)])
    thalach   = FloatField("Maximum Heart Rate Achieved(thalach)",
               validators=[InputRequired(), NumberRange(0,300)])
    exang   = FloatField("Exercise Induced Angina(exang)",
               validators=[InputRequired(), NumberRange(0,1)])
    oldpeak   = FloatField("ST Depression Induced By Exercise Relative To Rest(oldpeak)",
               validators=[InputRequired(), NumberRange(0,10)])
    slope   = FloatField("Slope Of The Peak Exercise ST Segment(slope)",
               validators=[InputRequired(), NumberRange(0,2)])
    ca   = FloatField("Number Of Major Vessels Colored By Flourosopy(ca)",
               validators=[InputRequired(), NumberRange(0,4)])
    thal   = FloatField("Normal, Fixed Defect, Reversable Defect(thal)",
               validators=[InputRequired(), NumberRange(0,3)])
    submit = SubmitField("Predict")

class SignUpForm(FlaskForm):
    email   = StringField("Email", validators=[InputRequired()])
    password   = PasswordField("Password", validators=[InputRequired()])
    name   = StringField("Name", validators=[InputRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[InputRequired()])
    password   = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Submit")
