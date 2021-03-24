#importing the necessary libraries
from flask import abort, jsonify, request, redirect
import flask
import json
import requests
import firebase_admin
from firebase_admin import auth,firestore,storage,credentials

#initialising the credentials
cred = credentials.Certificate("tinder-api-307fa-firebase-adminsdk-12d8z-48329730a7.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

#initializing the database
store=firestore.client()

# Initializing the flask
app=flask.Flask(__name__)

#creating new user
@app.route('/signUp',methods=['POST'])
def signUp():
    data=request.get_json(force=True)
    email_id=data.get('email')
    passwd=data.get('password')
    uid=""
    message=""
    try:
        user = auth.create_user(
        email=email_id,
        email_verified=False,
        password=passwd,
        disabled=False)
        uid=user.uid
        message="Sucessfully created new user:"
    except:
        message='User Already Exists'
    return jsonify({'Message':message,"UserID":uid,"Response":200})

#login with email
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json(force=True)
    email_id=data.get('email')
    passwd=data.get('password')
    uid=""
    message=""
    try:
        user = auth.get_user_by_email(email_id)
        uid=user.uid
        message="Succesfully login !!!"
    except:
        message="Email does not exist !!!"
    return jsonify({"Message":message,"Userid":uid,"Response":200})

#updating user data
@app.route('/updateUserData',methods=['POST'])
def updataUserData():
    user_data=request.get_json(force=True)
    uid=user_data.get('userid')
    user_details={}
    user_details['name']=user_data['name']
    user_details['phone_number']=user_data['phone_number']
    user_details['image']=user_data['image']
    user_details['desp']=user_data['desp']
    user_details['location']=user_data['location']
    user_details['dob']=user_data['dob']
    user_details['gender']=user_data['gender']
    user_details['passion']=user_data['passion']
    user_details['job']=user_data['job']
    user_details['company']=user_data['company']
    user_details['Created At']=firestore.SERVER_TIMESTAMP
    store.collection("Users").document(uid).set(user_details)
    return jsonify({"Message":"Succesfully update User Data","Userid":uid,"Response":200})

#getting feed based on city
@app.route('/feed',methods=['POST'])
def feed():
    data=request.get_json(force=True)
    uid=data.get('userid')
    city=data.get('city')
    gender=data.get('gender')
    docs=store.collection('Users').where("gender","==",gender).stream()
    swipes=store.collection('Swipes').stream()
    visited=[]
    for swipe in swipes:
        if (swipe.to_dict().get('uid_a')==uid):
            visited.append(swipe.to_dict().get('uid_b'))
    result={}
    #if person is not shown in feed 
    for doc in docs:
         #if he/she is a new user
        if (len(visited)==0) and (doc.to_dict().get('location').get('city')==city):
            result[doc.id]=doc.to_dict()
        if ((len(visited)!=0) and (doc.id not in visited)) and (doc.to_dict().get('location').get('city')==city):
            result[doc.id]=doc.to_dict()
    return jsonify(result)
    # return jsonify({"Name":result.get('name'),"Visited":visited,"Image":result.get('image'),"Description":result.get('desp'),"Passion":result.get('passion')})

#for swipe
@app.route('/swipe',methods=['POST'])
def swipe():
    data=request.get_json(force=True)
    userid_A=data['uid_a']
    userid_B=data['uid_b']
    is_right=data['is_right']
    is_left=data['is_left']
    result={}
    result['uid_a']=userid_A
    result['uid_b']=userid_B
    result['is_right']=is_right
    result['is_left']=is_left
    store.collection('Swipes').document(userid_A).set(result)
    return jsonify({"Response":200})

#getting match
@app.route('/match',methods=['POST'])
def match():
    data=request.get_json(force=True)
    userid_A=data['uid_a']
    userid_B=data['uid_b']
    result={}
    docs=store.collection('Swipes').stream()
    for doc in docs:
        if (userid_A in doc.id or userid_B in doc.id) and (doc.to_dict().get('is_right')):
            result['uid_a']=userid_A
            result['uid_b']=userid_B
            result['Matched']=True
            store.collection('Matched_Yes').document(userid_B).set(result)
            message= 'Congratulations !!! you both matched'
            return jsonify({'Message':message,"Result":result,"Response":200})

        else:
            result['uid_a']=userid_A
            result['uid_b']=userid_B
            result['Matched']=False
            store.collection('Matched_Yes').document(userid_B).set(result)
            message=""
            return jsonify({'Message':message,"Result":result,"Response":200})

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=False)

'''
You can check my app deployed on heroku by using following url
https://tinder-ironstark.herokuapp.com/
'''