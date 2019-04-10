from flask import Flask, request, redirect, render_template, url_for
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    user_name = request.form['user_name']
    password = request.form['password']
    re_password = request.form['re_password']
    email = request.form['email']

    error = False
    error_un = '' 
    error_pw = ''
    error_empty_un = ''
    error_empty_pw = ''
    error_re_pw = ''
    error_email_length = ''
    error_email_syntax = ''
    amp_counter = 0
    dot_counter = 0

    if not user_name:
        error_empty_un = "Please enter a username"
        error = True
    
    if not password:
        error_empty_pw = "Please enter a password"
        error = True

    if (0 < len(user_name) < 3) or (len(user_name) > 20):
        error_un = "Please enter a username between 3-20 characters"
        error = True

    if (0 < len(password) < 3) or (len(password) > 20):
        error_pw = "Please enter a password between 3-20 characters"
        error = True

    if password != re_password:
        error_re_pw="Please make sure that your password entries match"
        error = True
    
    if (0 < len(email) < 3) or (len(email) > 20):
        error_email_length = "Please enter an email between 3-20 characters"
        error = True

    for i in email:
        if i == '@':
            amp_counter += 1
        if i == '.':
            dot_counter += 1

    if len(email) != 0:
        if (amp_counter != 1) or (dot_counter != 1):
            error_email_syntax = "Please enter a valid email address (name@website.com)"
            error = True

    # email error 1: between 3 and 20 char
    # error 2 (or split into multiple if's): only one dot, one @, not spaces - REGEX 
    
    if error:
        return render_template('index.html', error_un=error_un, error_pw=error_pw, 
            error_empty_un=error_empty_un, error_empty_pw=error_empty_pw, error_re_pw=error_re_pw,
            error_email_length=error_email_length, error_email_syntax=error_email_syntax)

    else:
        return render_template('welcome.html', name=user_name)


app.run()