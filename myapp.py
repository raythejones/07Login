from flask import Flask, render_template, request, session
import os 

app = Flask(__name__)
app.secret_key = os.urandom(32)


#test account info
username = 'ray'
password = 'jones'

@app.route('/')
def root():
    if session.has_key('name'):
        return render_template('greeting.html', myUser = session['name'])
    else: 
        return render_template('home.html')

@app.route('/route', methods = ['POST'])
def route():
    if request.form['myUser'] == username:
        session['name'] = request.form['myUser']
        return render_template('greeting.html', myUser = request.form['myUser'])
    else:
        return render_template('home.html', message = "username or password incorrect")



if __name__ == '__main__':
    app.debug = True
    app.run()