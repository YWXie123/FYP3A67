from application import app, ai_model, db
from application.forms import PredictionForm, LoginForm, SignUpForm
from flask import render_template, request, flash, json, jsonify, redirect
from application.models import Entry, User
from datetime import datetime
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash

#Global list for look up
heart_disease = ['No heart disease','Has heart disease']
#create the database if not exist
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET','POST'])
def login_post():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', title="Login", form=form, index=True)

    if request.method == 'POST':  
        if form.validate_on_submit():      
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                flash('Please check your login details and try again.')
                return redirect("/login")

            login_user(user)
        else:
            flash("Error, cannot proceed with login","danger")

    return redirect("/")


@app.route('/signup', methods=['GET','POST'])
def signup_post():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html',title="Sign Up", form=form, index=True)

    if request.method == 'POST':
        if form.validate_on_submit(): 
            email = form.email.data
            name = form.name.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user:
                flash('Email address already exists.')
                return redirect("/login")

            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
        else:
            flash("Error, cannot proceed with sign up","danger")

    return redirect("/login")

@app.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect("/login")



#Handles http://127.0.0.1:5000/
@app.route('/') 
@app.route('/index') 
@app.route('/home') 
@login_required
def index_page(): 
    form = PredictionForm()
    return render_template("index.html",form=form , title=
                       "Enter Heart Disease Prediction", entries = get_entries(), 
                       heart_disease=heart_disease)

@app.route("/predict", methods=['GET','POST'])
@login_required
def predict():
    form = PredictionForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            age = form.age.data
            sex = form.sex.data
            cp = form.cp.data
            trestbps = form.trestbps.data
            chol = form.chol.data
            fbs = form.fbs.data
            restecg = form.restecg.data
            thalach = form.thalach.data
            exang = form.exang.data
            oldpeak = form.oldpeak.data
            slope = form.slope.data
            ca = form.ca.data
            thal = form.thal.data
            fk_userId = current_user.id
            X = [[ age, sex,  cp,  trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            result = ai_model.predict(X)
            result_prob = ai_model.predict_proba(X)
            new_entry = Entry(age=age, sex=sex, cp=cp, trestbps=trestbps,
                        chol=chol, fbs=fbs, restecg=restecg, thalach=thalach,
                        exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal,fk_userId=fk_userId,
                        prediction=int(result[0]), 
                        predicted_on=datetime.utcnow())
            add_entry(new_entry)
            flash(f"Prediction: {heart_disease[result[0]]}, Probability of Prediction: {result_prob[:, result[0]][0]*100:.2f}%","success")
            # flash(f"Probability of Prediction: {result_prob[:, result[0]][0]*100:.2f}%","success")
        else:
            flash("Error, cannot proceed with prediction","danger")
    return render_template("index.html", title="Enter Heart Disease Prediction", form=form, index=True, 
                            entries = get_entries(), heart_disease=heart_disease)

@app.route('/remove', methods=['POST','GET'])
@login_required
def remove():
    if request.method == 'POST':
        form = PredictionForm()
        req = request.form
        id = req["id"]
        remove_entry(id)
    return redirect("/")

#API: add entry
@app.route("/api/add", methods=['POST'])
def api_add(): 
    #retrieve the json file posted from client
    data = request.get_json()
    #retrieve each field from the data
    age     = data['age']
    sex     = data['sex']
    cp     = data['cp']
    trestbps     = data['trestbps']
    chol     = data['chol']
    fbs     = data['fbs']
    restecg     = data['restecg']
    thalach     = data['thalach']
    exang     = data['exang']
    oldpeak     = data['oldpeak']
    slope     = data['slope']
    ca     = data['ca']
    thal     = data['thal']
    prediction  = data['prediction']
    #create an Entry object store all data for db action
    new_entry = Entry(  age=age, sex=sex,
                        cp=cp,trestbps=trestbps,
                        chol=chol, fbs=fbs,
                        restecg=restecg,thalach=thalach,
                        exang=exang, oldpeak=oldpeak,
                        slope=slope, ca=ca, thal=thal,
                        prediction = prediction,  
                        predicted_on=datetime.utcnow())
    #invoke the add entry function to add entry                        
    result = add_entry(new_entry)
    #return the result of the db action
    return jsonify({'id':result})

def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id

    except Exception as error:
        db.session.rollback()
        flash(error,"danger")

def get_entries():
    try:
        entries =  Entry.query.filter_by(fk_userId = current_user.id).all()
        return entries
    except Exception as error:
        db.session.rollback()
        flash(error,"danger") 
        return 0

def test_get_entries():
    try:
        entries =  Entry.query.all()
        return entries
    except Exception as error:
        db.session.rollback()
        flash(error,"danger") 
        return 0

def get_entry(id):
    try:
        entries = Entry.query.filter(Entry.id==id)
        result = entries[0]
        return result
    except Exception as error:
        db.session.rollback()
        flash(error,"danger") 
        return 0

#API get entry
@app.route("/api/get/<id>", methods=['GET'])
def api_get(id): 
    #retrieve the entry using id from client
    entry = get_entry(int(id))
    #Prepare a dictionary for json conversion
    data = {'id'        : entry.id,
            'age'   : entry.age, 
            'sex'   : entry.sex,
            'cp'   : entry.cp,
            'trestbps'   : entry.trestbps,
            'chol'   : entry.chol, 
            'fbs'   : entry.fbs,
            'restecg'   : entry.restecg,
            'thalach'   : entry.thalach,
            'exang'   : entry.exang, 
            'oldpeak'   : entry.oldpeak,
            'slope'   : entry.slope,
            'ca'   : entry.ca,
            'thal'   : entry.thal,
            'prediction': entry.prediction}
    #Convert the data to json
    result = jsonify(data)
    return result #response back

#API get all entry
@app.route("/api/get", methods=['GET'])
def api_get_all_entry(): 
    entries = test_get_entries()
    datalist=[]
    #Prepare a dictionary for json conversion

    for entry in entries:
        datalist.append({'id'        : entry.id,
                'age'   : entry.age, 
                'sex'   : entry.sex,
                'cp'   : entry.cp,
                'trestbps'   : entry.trestbps,
                'chol'   : entry.chol, 
                'fbs'   : entry.fbs,
                'restecg'   : entry.restecg,
                'thalach'   : entry.thalach,
                'exang'   : entry.exang, 
                'oldpeak'   : entry.oldpeak,
                'slope'   : entry.slope,
                'ca'   : entry.ca,
                'thal'   : entry.thal,
                'prediction': entry.prediction})
    
    #Convert the data to json
    result = jsonify(datalist)
    return result #response back

#API delete entry
@app.route("/api/delete/<id>", methods=['GET'])
def api_delete(id): 
    entry = remove_entry(int(id))
    return jsonify({'result':'ok'})

def remove_entry(id):
    try:
        entry = Entry.query.get(id)
        db.session.delete(entry)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")


# Test for prediction
@app.route("/api/predict", methods=['GET', 'POST'])
def api_predict():
    #retrieve the json file posted from client
    data = request.get_json()
    #retrieve each field from the data
    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trestbps = data['trestbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalach = data['thalach']
    exang = data['exang']
    oldpeak = data['oldpeak']
    slope = data['slope']
    ca = data['ca']
    thal = data['thal']

    X = [[ age, sex,  cp,  trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    result = ai_model.predict(X)
    print(f"Result: {int(result[0])}")
    result_proba = ai_model.predict_proba(X)
    return jsonify({'prediction': int(result[0]), 'predict_proba': round(result_proba[0][result[0]]*100, 2)})

