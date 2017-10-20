from flask import Flask, render_template, request, session
import os 

myapp = Flask(__name__)
myapp.secret_key = os.urandom(32)


#test user and pass
username = 'ray'
password = 'jones'

@myapp.route('/')
def root():
#if a user's logged in already
    if session.has_key('username'):
        return render_template('welcome.html', myUser = session['username'])
#if not
    else: 
        return render_template('home.html')

@myapp.route('/route', methods = ['POST'])
def route():
    if request.form['username'] == username and request.form['password'] == password:
        session['username'] = request.form['username']
        return render_template('welcome.html', myUser = request.form['username'])
    else:
#display an error on the form page    
        return render_template('home.html', message = "username or password is incorrect")

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()