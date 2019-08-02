import os
from app import app
from flask import render_template, request, redirect, session, url_for

from flask_pymongo import PyMongo
app.secret_key= b'\xa0C\xf8\x87\x1b31\xd6\x1fvB\x1b\xee\x07Bq'

# name of database
app.config['MONGO_DBNAME'] = 'login' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:1234567890@cluster0-tctju.mongodb.net/login?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


# CONNECT TO DB, ADD DATA

# @app.route('/add')

# def add():
#     # connect to the database

#     # insert new data

#     # return a message to the user
#     return ""

# sign-up
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method =="POST":
        #take in the info they gave us, check if username is taken, if username is available, put into a databse of users
        users= mongo.db.users
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user is None:
            users.insert({"username":request.form['username'], "password":request.form['password'], "first-name":request.form['first-name'], "last-name":request.form['last-name'], 'email':request.form['email'], 'phone-number':request.form['phone-number']})
            return render_template('accountconfirmation.html')
        else:
            message = "Username already taken. Try logging in, or try a different username."
            return render_template('signup.html', message= message)
    else:   
        return render_template('signup.html', message= "")
        
#Log In:
@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method== 'POST':
        users = mongo.db.users
        #use the username to find the account
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user: 
          # check if the password is right
          if existing_user['password'] == request.form['password'] :
              session['username'] = request.form['username']
              username= str(session['username'])
              print(username)
              return redirect(url_for('index'))
          else:
              message = "Incorrect username or password. Please try again."
              return render_template('login.html', message= message)
        else:
            message = "There is no user with that usermame. Try making an account."
            return render_template('login.html', message= message)
    else:
        return render_template('login.html', message= "")
            
        
#Log Out:
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
#Mission Statement:
@app.route('/missionstatement')
def missionstatement():
    return render_template('missionstatement.html')
    
#Finaces 
@app.route('/finances', methods= ["GET", "POST"])
def finaces():
    if request.method== "GET":
        tasks= mongo.db.tasks
        tasks= tasks.find()
        return render_template('finances.html', tasks=tasks)
    
    # connect to the database
    else:
        tasks= mongo.db.tasks
        # insert new data
        userdata = dict(request.form)
        tasks.insert(userdata)
        print(userdata)
        tasks= tasks.find()
        # return a message to the user
        return render_template('finances.html', tasks=tasks)

#Customers
@app.route('/customer')
def customer():
    return render_template('customer.html')
    
#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Subcription
@app.route('/subscription', methods = ['GET', 'POST'])
def subscription():
    if request.method =="POST":
        #take in the info they gave us, check if username is taken, if username is available, put into a databse of users
        subscription= mongo.db.subscription
        existing_subscription = subscription.find_one({"organization":request.form["organization"]})
        if existing_subscription is None:
            subscription.insert({"package":request.form['package'], "organization":request.form['organization'], "cardtype":request.form['cardtype'], "cardholder-name":request.form['cardholder-name'], 'card-number':request.form['card-number'], 'expiration-date':request.form['expiration-date'], 'zip-code':request.form['zip-code']})
            return render_template('subscriptionsuccessful.html')
        else:
            message = "There is already an account associated with this organization. Please ask an administrator or use a different organization."
            return render_template('subscription.html', message= message)
    else:   
        return render_template('subscription.html', message= "")
        