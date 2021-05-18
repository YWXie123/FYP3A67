from application.models import Staff
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

def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
 
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")

@app.route('/login/add', methods=['POST'])
def api_add_login():
    #retrieve the json file posted
    data = request.get_json()
    #retrieve each field from the data
    id = data['id']
    staffid = data['staffid']
    name = data['name']
    position = data['position']
    department = data['department']
    #create an Entry object store all data for db action
    new_entry = Staff(  id = id, staffid = staffid,
                        name = name, position = position,
                        department=department)

@app.route('/ask/add', methods=['POST'])
def api_add_qns():
    #retrieve the json file posted
    data = request.get_json()
    #retrieve each field from the data
    id = data['id']
    staffid = data['staffid']
    question = data['question']
    #create an Entry object store all data for db action
    new_entry = Staff(  id = id, staffid = staffid,
                        asked_on=datetime.utcnow(),
                        question = question)
