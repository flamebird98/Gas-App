#!/usr/bin/env python
from flask import Flask, render_template, request, session, redirect
from flask_httpauth import HTTPBasicAuth
import cgi, cgitb, time
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
import logging
import messaging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		msg = messaging.Messaging()
		msg.send('GETHASH', {'email': email })
		response = msg.receive()
		if response['success'] != True:
			return "Please try logging in again."
		if check_password_hash(response['hash'], password):
			session['email'] = email
			return redirect('/')
		else:
			return "Login failed."
	return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        msg = messaging.Messaging()
        msg.send(
            'REGISTER',
            {
                'fname': fname,
                'lname': lname,
                'email': email,
                'hash': generate_password_hash(password)
            }
        )
        response = msg.receive()
        if response['success']:
            session['email'] = email
            return redirect('/')
        else:
            return f"{response['message']}"
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')



