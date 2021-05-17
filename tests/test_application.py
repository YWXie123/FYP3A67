#1: Import libraries need for the test
from application.models import Entry, User
import datetime as datetime
import pytest
from flask import json
 
#Unit Test
#2: Parametrize section contains the data for the test
@pytest.mark.parametrize("entrylist",[
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1],  #Test integer arguments
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1]   
])
#3: Write the test function pass in the arguments
def test_EntryClass(entrylist,capsys):
    with capsys.disabled():
        print(entrylist)
        now = datetime.datetime.utcnow()
        new_entry = Entry(  age= entrylist[0], 
                            sex = entrylist[1],
                            cp= entrylist[2],
                            trestbps = entrylist[3],
                            chol  = entrylist[4], 
                            fbs= entrylist[5], 
                            restecg = entrylist[6],
                            thalach= entrylist[7],
                            exang = entrylist[8],
                            oldpeak  = entrylist[9],
                            slope= entrylist[10], 
                            ca = entrylist[11],
                            thal= entrylist[12],
                            prediction  = entrylist[13], 
                            predicted_on= now) 
 
        assert new_entry.age == entrylist[0]
        assert new_entry.sex == entrylist[1]
        assert new_entry.cp == entrylist[2]
        assert new_entry.trestbps == entrylist[3]
        assert new_entry.chol  == entrylist[4]
        assert new_entry.fbs == entrylist[5]
        assert new_entry.restecg == entrylist[6]
        assert new_entry.thalach == entrylist[7]
        assert new_entry.exang == entrylist[8]
        assert new_entry.oldpeak  == entrylist[9]
        assert new_entry.slope == entrylist[10]
        assert new_entry.ca == entrylist[11]
        assert new_entry.thal == entrylist[12]
        assert new_entry.prediction     == entrylist[13]
        assert new_entry.predicted_on   == now

@pytest.mark.parametrize("entrylist",[
    [  'xyw.gmail.com','123','xyw'],  #Test integer arguments
    [  'doaa.gmail.com','123','doaa']   
])
#3: Write the test function pass in the arguments
def test_UserClass(entrylist,capsys):
    with capsys.disabled():
        print(entrylist)
        new_entry = User(  email= entrylist[0], 
                            password = entrylist[1],
                            name= entrylist[2],
                            ) 
 
        assert new_entry.email == entrylist[0]
        assert new_entry.password == entrylist[1]
        assert new_entry.name == entrylist[2]

@pytest.mark.xfail(reason="arguments <= 0")
@pytest.mark.parametrize("entrylist",[
    [  63,  1,  -3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1],
    [  63,  1,  3,  145, -233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1] 
])
def test_EntryValidation(entrylist,capsys):
    test_EntryClass(entrylist,capsys)

@pytest.mark.parametrize("entrylist",[
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1],  #Test integer arguments
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1],
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1]    
])
def test_addAPI(client,entrylist,capsys):
    with capsys.disabled():
        #prepare the data into a dictionary
        data1 = {   'age': entrylist[0], 
                    'sex' : entrylist[1],
                    'cp': entrylist[2],
                    'trestbps' : entrylist[3],
                    'chol': entrylist[4], 
                    'fbs' : entrylist[5],
                    'restecg': entrylist[6],
                    'thalach' : entrylist[7],
                    'exang': entrylist[8], 
                    'oldpeak' : entrylist[9],
                    'slope': entrylist[10],
                    'ca' : entrylist[11],
                    'thal' : entrylist[12],
                    'prediction'  : entrylist[13]}
        #use client object  to post
        #data is converted to json
        #posting content is specified
        response = client.post('/api/add', 
            data=json.dumps(data1),
            content_type="application/json",)
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"]


#Test get API
@pytest.mark.parametrize("entrylist",[
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1, 1],  #Test integer arguments
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1, 2]  
])
def test_getAPI(client,entrylist,capsys):
    with capsys.disabled():
        response = client.get(f'/api/get/{entrylist[14]}')
        ret = json.loads(response.get_data(as_text=True))
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        print('response:',response_body)
        assert response_body["id"] == entrylist[14]
        assert response_body["age"] == float(entrylist[0])
        assert response_body["sex"] == float(entrylist[1])
        assert response_body["cp"] == float(entrylist[2])
        assert response_body["trestbps"] == float(entrylist[3])
        assert response_body["chol"] == float(entrylist[4])
        assert response_body["fbs"] == float(entrylist[5])
        assert response_body["restecg"] == float(entrylist[6])
        assert response_body["thalach"] == float(entrylist[7])
        assert response_body["exang"] == float(entrylist[8])
        assert response_body["oldpeak"] == float(entrylist[9])
        assert response_body["slope"] == float(entrylist[10])
        assert response_body["ca"] == float(entrylist[11])
        assert response_body["thal"] == float(entrylist[12])
        assert response_body["prediction"] == float(entrylist[13])

#Test get all API
@pytest.mark.parametrize("entrylist",[
    [[  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1, 1],  #Test integer arguments
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1, 2],
    [  63,  1,  3,  145, 233,  1,  0,  150, 1,  2.3,  0, 0, 1, 1, 3]]   
])
def test_get_all_entry (client,entrylist,capsys):
    with capsys.disabled():
        response = client.get(f'/api/get')
        ret = json.loads(response.get_data(as_text=True))
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        for i, res in enumerate(response_body):
            assert res["id"] == entrylist[i][14]
            assert res["age"] == float(entrylist[i][0])
            assert res["sex"] == float(entrylist[i][1])
            assert res["cp"] == float(entrylist[i][2])
            assert res["trestbps"] == float(entrylist[i][3])
            assert res["chol"] == float(entrylist[i][4])
            assert res["fbs"] == float(entrylist[i][5])
            assert res["restecg"] == float(entrylist[i][6])
            assert res["thalach"] == float(entrylist[i][7])
            assert res["exang"] == float(entrylist[i][8])
            assert res["oldpeak"] == float(entrylist[i][9])
            assert res["slope"] == float(entrylist[i][10])
            assert res["ca"] == float(entrylist[i][11])
            assert res["thal"] == float(entrylist[i][12])
            assert res["prediction"] == float(entrylist[i][13])

#Test delete API
@pytest.mark.parametrize("ind",[1,2])
def test_deleteAPI(client,ind,capsys):
    with capsys.disabled():
        response = client.get(f'/api/delete/{ind}')
        ret = json.loads(response.get_data(as_text=True))
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["result"] == "ok"

# test prediction
@pytest.mark.parametrize("entrylist", [
    [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1, 1],
    [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2, 1]
])
def test_predictAPI(client,entrylist,capsys):
    with capsys.disabled():
        #prepare the data into a dictionary
        data1 = {   'age': entrylist[0], 
                    'sex' : entrylist[1],
                    'cp': entrylist[2],
                    'trestbps' : entrylist[3],
                    'chol' : entrylist[4],
                    'fbs' : entrylist[5],
                    'restecg' : entrylist[6],
                    'thalach' : entrylist[7],
                    'exang' : entrylist[8],
                    'oldpeak' : entrylist[9],
                    'slope' : entrylist[10],
                    'ca' : entrylist[11],
                    'thal' : entrylist[12]}
        #use client object  to post
        #data is converted to json
        #posting content is specified
        response = client.post('/api/predict', 
            data=json.dumps(data1),
            content_type="application/json",)
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert entrylist[-1] == response_body['prediction']
        # assert response_body['prediction'] 
        assert response_body['predict_proba']
        