#!flask/bin/python

from flask import Flask, jsonify, request, render_template, url_for
import sys
import os
import time

app = Flask(__name__, template_folder="/home/ubuntu/naca_airfoil")

@app.route('/')
def form():
	return render_template('form_submit.html')

@app.route('/runsh/', methods=['POST'])
def runsh():
	angle_start=request.form['angle_start']
	angle_stop=request.form['angle_stop']
	n_angles=request.form['n_angles']
	n_nodes=request.form['n_nodes']
	n_levels=request.form['n_levels']
	return render_template('runsh.html', angle_start=angle_start, angle_stop=angle_stop, n_angles=n_angles, n_nodes=n_nodes, n_levels=n_levels)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True )