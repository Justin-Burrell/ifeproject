import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'login-name' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:1234567890@cluster0-tctju.mongodb.net/login?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""

@app.route('/signup' , methods= ["GET", "POST"])
def signup():
    if method== "GET":
        return render_template('signup.html')
    elif method== "POST":
        