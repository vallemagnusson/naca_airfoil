#!flask/bin/python

from flask import Flask, jsonify, request, render_template
import sys
import os
import time

app = Flask(__name__)

@app.route("/messaging", methods=['GET'])
def compute_drag_free_landing(initial_velocity, initial_angle):
	return landing_point

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
@app.route("/input", methods=['GET', 'PUT'])
def input():
	error = None
	if request.method == 'PUT':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	# the code below is executed if the request method
	# was GET or the credentials were invalid
	return render_template('login.html', error=error)


#def start():
#	return "sidan fungerar", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True )