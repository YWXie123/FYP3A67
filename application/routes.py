from application.forms import LoginForm
from application import app

from flask import render_template

#Handles http://127.0.0.1:5000/hello
@app.route('/') 
def hello_world(): 
    return "<h1>Hello World</h1>"

@app.route('/login') 
def login_page(): 
    form = LoginForm()
    return render_template("login.html", form=form)
