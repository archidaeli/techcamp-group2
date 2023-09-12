#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import requests
# from pymongo import MongoClient
import jinja2.exceptions

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# MongoDB Configuration
# client = MongoClient("mongodb+srv://mntbdjw:<password>@csr.rur1bj0.mongodb.net/")  # Replace with your MongoDB connection URL
# db = client["final_project"]
# users = db["users"]

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        # email = request.form['email']
        # password = request.form['password']
        # hashed_password = generate_password_hash(password, method='sha256')
        # user_data = {
        #     'email': email,
        #     'password': hashed_password
        # }
        # users.insert_one(user_data)
    return 204
        # return redirect(url_for('login'))
    # return render_template('register.html')

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        return 'Invalid username or password'
    return render_template('login.html')

@app.route('/upload/data', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = {
            'index': 4,  # Your integer value
            'url': 'https://images.remotehub.com/d42c62669a7711eb91397e038280fee0/original_thumb/ec1eb042.jpg'
        }

        response = requests.post('https://9664-2001-448a-2012-1fe7-e65c-2fdd-d673-5693.ngrok-free.app/', json=data)
        print(response.data)

    return render_template('trashbin.html'), 200



# # User Dashboard Route
# @app.route('/dashboard')
# def dashboard():
#     if 'user' in session:
#         return f'Logged in as {session["user"]}'
#     return 'You are not logged in.'

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
