from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, PasswordField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange

class PredictionForm(FlaskForm):
    question = StringField("Question here",
                validators = [InputRequired()])
    submit = SubmitField("Predict")

class SignUpForm(FlaskForm):
    password   = PasswordField("Password", validators=[InputRequired()])
    name   = StringField("Name", validators=[InputRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[InputRequired()])
    password   = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Submit")
