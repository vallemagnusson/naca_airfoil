#!flask/bin/python

from flask import Flask, jsonify, request, render_template, url_for
import sys
import os
import time

app = Flask(__name__, template_folder="/home/ubuntu/naca_airfoil")

@app.route("/messaging", methods=['GET'])
def compute_drag_free_landing(initial_velocity, initial_angle):
	return landing_point

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
#@app.route("/input", methods=['GET', 'PUT'])
#def input():
#	error = None
#	if request.method == 'PUT':
#		if valid_login(request.form['username'],request.form['password']):
#			return log_the_user_in(request.form['username'])
#		else:
#			error = 'Invalid username/password'
#	# the code below is executed if the request method
#	# was GET or the credentials were invalid
#	return render_template('login.html', error=error)

@app.route('/index/', methods=['GET','POST'])
def hello_world():
	author = "vama"
	name = "Valle Magnusson"
	#return app.root_path
	return render_template('index.html', author=author, name=name)

@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/hello/', methods=['POST'])
def hello():
	name=request.form['yourname']
	email=request.form['youremail']
	return render_template('form_action.html', name=name, email=email)

#if __name__ == "__main__":
#	app.run(host="0.0.0.0", debug=True )
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )